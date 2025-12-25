#!/usr/bin/env python3
"""
PostgreSQL to MySQL Data Migration Script for Dify

This script migrates all data from PostgreSQL to MySQL using SQLAlchemy Core.
It uses Dify's table metadata and SQLAlchemy's type system for automatic type conversion.

Key features:
    - Preserves all field values including updated_at timestamps
    - Automatic JSON serialization for dict/list fields
    - Batch processing for large tables

Usage:
    uv run --project api python scripts/migrate_pg_to_mysql.py

Prerequisites:
    - MySQL tables already created via: flask db upgrade
    - PostgreSQL database with data
    - Update connection strings in this script or use environment variables
"""

import sys
from pathlib import Path

# Add api directory to path
api_dir = Path(__file__).parent.parent
sys.path.insert(0, str(api_dir))

import click
from sqlalchemy import create_engine, text, func
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection
PG_URL = "postgresql://postgres:difyai123456@localhost:5432/dify"

# MySQL connection  
MYSQL_URL = "mysql+pymysql://root:difyai123456@localhost:2881/dify"

# Batch size for migration
BATCH_SIZE = 1000


def get_all_table_models():
    """
    Automatically discover all Dify tables.
    Returns a list of (table, table_name) tuples.
    """
    # Import all models from Dify to ensure metadata is populated
    from models.base import TypeBase
    
    # Get all tables from metadata
    tables = []
    for table_name, table in TypeBase.metadata.tables.items():
        tables.append((table, table_name))
    
    return sorted(tables, key=lambda x: x[1])  # Sort by table name


def migrate_table(pg_session_factory, mysql_session_factory, table, table_name):
    """
    Migrate a single table using direct SQL queries.
    
    Args:
        pg_session_factory: PostgreSQL session factory
        mysql_session_factory: MySQL session factory
        table: SQLAlchemy Table object
        table_name: Table name
    
    Returns:
        Number of rows migrated
    """
    from sqlalchemy import select, insert
    
    click.echo(f"Migrating {table_name}...")
    
    total_migrated = 0
    offset = 0
    
    try:
        with pg_session_factory() as pg_session:
            # Get total count
            count_query = select(func.count()).select_from(table)
            total_count = pg_session.execute(count_query).scalar()
            
            if total_count == 0:
                click.echo(f"  {table_name}: Empty table, skipping")
                return 0
            
            click.echo(f"  Total rows: {total_count}")
            
            # Migrate in batches
            with click.progressbar(length=total_count, label=f"  Progress") as bar:
                while offset < total_count:
                    # Read batch from PostgreSQL
                    select_query = select(table).offset(offset).limit(BATCH_SIZE)
                    pg_rows = pg_session.execute(select_query).fetchall()
                    
                    if not pg_rows:
                        break
                    
                    # Write batch to MySQL
                    with mysql_session_factory() as mysql_session:
                        # Convert rows to dictionaries
                        rows_data = []
                        for row in pg_rows:
                            row_dict = dict(row._mapping)
                            rows_data.append(row_dict)
                        
                        # Bulk insert
                        if rows_data:
                            mysql_session.execute(insert(table), rows_data)
                            mysql_session.commit()
                    
                    total_migrated += len(pg_rows)
                    offset += BATCH_SIZE
                    bar.update(len(pg_rows))
        
        click.echo(click.style(f"✓ {table_name}: {total_migrated} rows migrated", fg="green"))
        return total_migrated
        
    except Exception as e:
        click.echo(click.style(f"✗ {table_name}: Failed - {str(e)}", fg="red"))
        import traceback
        traceback.print_exc()
        return 0


def verify_migration(pg_engine, mysql_engine, table_name):
    """
    Verify that the data was migrated correctly.
    
    Returns:
        (pg_count, mysql_count, match)
    """
    with pg_engine.connect() as pg_conn:
        result = pg_conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
        pg_count = result.scalar()
    
    with mysql_engine.connect() as mysql_conn:
        result = mysql_conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
        mysql_count = result.scalar()
    
    return pg_count, mysql_count, pg_count == mysql_count


@click.command()
@click.option("--pg-url", default=PG_URL, help="PostgreSQL connection URL")
@click.option("--mysql-url", default=MYSQL_URL, help="MySQL connection URL")
@click.option("--batch-size", default=BATCH_SIZE, help="Batch size for migration")
@click.option("--verify/--no-verify", default=True, help="Verify after migration")
@click.option("--tables", help="Comma-separated list of specific tables to migrate")
def main(pg_url, mysql_url, batch_size, verify, tables):
    """
    Migrate all data from PostgreSQL to MySQL using SQLAlchemy Core.
    """
    global BATCH_SIZE
    BATCH_SIZE = batch_size
    
    click.echo("=" * 80)
    click.echo("Dify Data Migration: PostgreSQL → MySQL")
    click.echo("=" * 80)
    click.echo()
    
    # Create database engines
    click.echo("Connecting to databases...")
    pg_engine = create_engine(pg_url)
    mysql_engine = create_engine(mysql_url)
    
    # Create session factories
    PgSession = sessionmaker(bind=pg_engine)
    MySQLSession = sessionmaker(bind=mysql_engine)
    
    # Verify connections
    try:
        with pg_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        click.echo("✓ PostgreSQL connection successful")
    except Exception as e:
        click.echo(click.style(f"✗ PostgreSQL connection failed: {e}", fg="red"))
        return
    
    try:
        with mysql_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        click.echo("✓ MySQL connection successful")
    except Exception as e:
        click.echo(click.style(f"✗ MySQL connection failed: {e}", fg="red"))
        return
    
    click.echo()
    
    # Get all models
    click.echo("Discovering Dify models...")
    all_models = get_all_table_models()
    click.echo(f"Found {len(all_models)} tables to migrate")
    click.echo()
    
    # Filter tables if specified
    if tables:
        table_list = [t.strip() for t in tables.split(',')]
        all_models = [(m, t) for m, t in all_models if t in table_list]
        click.echo(f"Filtering to {len(all_models)} specified tables")
        click.echo()
    
    # Disable foreign key checks in MySQL (for safety, though not needed)
    with mysql_engine.connect() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        conn.commit()
    
    # Migrate all tables
    total_rows = 0
    successful_tables = 0
    failed_tables = []
    
    for table, table_name in all_models:
        migrated = migrate_table(PgSession, MySQLSession, table, table_name)
        if migrated >= 0:
            total_rows += migrated
            successful_tables += 1
        else:
            failed_tables.append(table_name)
        click.echo()
    
    # Re-enable foreign key checks
    with mysql_engine.connect() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))
        conn.commit()
    
    # Summary
    click.echo("=" * 80)
    click.echo("Migration Summary")
    click.echo("=" * 80)
    click.echo(f"Total tables: {len(all_models)}")
    click.echo(f"Successful: {successful_tables}")
    click.echo(f"Failed: {len(failed_tables)}")
    if failed_tables:
        click.echo(f"Failed tables: {', '.join(failed_tables)}")
    click.echo(f"Total rows migrated: {total_rows}")
    click.echo()
    
    # Verification
    if verify:
        click.echo("=" * 80)
        click.echo("Verifying Migration")
        click.echo("=" * 80)
        click.echo()
        
        mismatched = []
        for table, table_name in all_models:
            pg_count, mysql_count, match = verify_migration(pg_engine, mysql_engine, table_name)
            status = "✓" if match else "✗"
            color = "green" if match else "red"
            
            click.echo(
                click.style(
                    f"{status} {table_name:40} PG: {pg_count:8} MySQL: {mysql_count:8}",
                    fg=color
                )
            )
            
            if not match:
                mismatched.append(table_name)
        
        click.echo()
        if mismatched:
            click.echo(click.style(f"✗ {len(mismatched)} tables have mismatched counts!", fg="red"))
            click.echo(f"Mismatched tables: {', '.join(mismatched)}")
        else:
            click.echo(click.style("✓ All table counts verified successfully!", fg="green"))
    
    click.echo()
    click.echo("=" * 80)
    click.echo(click.style("Migration completed!", fg="green"))
    click.echo("=" * 80)


if __name__ == "__main__":
    main()
