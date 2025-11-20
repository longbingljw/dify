#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path

try:
    from dotenv import load_dotenv
    import pymysql
except ImportError as e:
    print(f"Required packages not installed: {e}")
    print("Please install: pip install python-dotenv PyMySQL")
    exit(1)

# Load .env
env_file = Path("api/.env")
if env_file.exists():
    load_dotenv(env_file)

# Get current values from .env or defaults
current_values = {
    'db_username': os.getenv('DB_USERNAME', 'root'),
    'db_password': os.getenv('DB_PASSWORD', 'difyai123456'),
    'db_host': os.getenv('DB_HOST', 'localhost'),
    'db_port': int(os.getenv('DB_PORT', '3306')),
    'db_database': os.getenv('DB_DATABASE', 'mysql')
}

# Prompt user for new values
print("请输入数据库配置 (按回车使用当前值):")
print()

db_username = input(f"DB_USERNAME [{current_values['db_username']}]: ").strip()
db_password = input(f"DB_PASSWORD [{current_values['db_password']}]: ").strip()
db_host = input(f"DB_HOST [{current_values['db_host']}]: ").strip()
db_port = input(f"DB_PORT [{current_values['db_port']}]: ").strip()
db_database = input(f"DB_DATABASE [{current_values['db_database']}]: ").strip()

# Use current values if empty input
if not db_username:
    db_username = current_values['db_username']
if not db_password:
    db_password = current_values['db_password']
if not db_host:
    db_host = current_values['db_host']
if not db_port:
    db_port = str(current_values['db_port'])
else:
    try:
        db_port = str(int(db_port))  # Validate it's a number
    except ValueError:
        print("Invalid port number, using current value")
        db_port = str(current_values['db_port'])
if not db_database:
    db_database = current_values['db_database']

def manage_database(db_config):
    """Create or recreate database if needed."""
    print(f"Checking database '{db_config['database']}'...")

    try:
        # Connect without specifying database
        connection = pymysql.connect(
            host=db_config['host'],
            port=db_config['port'],
            user=db_config['username'],
            password=db_config['password']
        )
        cursor = connection.cursor()

        # Check if database exists
        cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in cursor.fetchall()]

        if db_config['database'] in databases:
            print(f"Database '{db_config['database']}' exists, dropping and recreating...")
            cursor.execute(f"DROP DATABASE `{db_config['database']}`")
            print(f"Database '{db_config['database']}' dropped successfully")
        else:
            print(f"Database '{db_config['database']}' does not exist, creating...")

        # Create new database
        cursor.execute(f"CREATE DATABASE `{db_config['database']}`")
        print(f"Database '{db_config['database']}' created successfully")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Database operation failed: {e}")
        exit(1)

# Update .env file
if env_file.exists():
    with open(env_file, 'r') as f:
        content = f.read()

    content = content.replace(f"DB_USERNAME={current_values['db_username']}", f"DB_USERNAME={db_username}")
    content = content.replace(f"DB_PASSWORD={current_values['db_password']}", f"DB_PASSWORD={db_password}")
    content = content.replace(f"DB_HOST={current_values['db_host']}", f"DB_HOST={db_host}")
    content = content.replace(f"DB_PORT={current_values['db_port']}", f"DB_PORT={db_port}")
    content = content.replace(f"DB_DATABASE={current_values['db_database']}", f"DB_DATABASE={db_database}")

    with open(env_file, 'w') as f:
        f.write(content)

    # Reload environment variables after updating .env
    load_dotenv(env_file)

    # Set environment variables for the subprocess
    env = os.environ.copy()
    env['DB_USERNAME'] = db_username
    env['DB_PASSWORD'] = db_password
    env['DB_HOST'] = db_host
    env['DB_PORT'] = db_port
    env['DB_DATABASE'] = db_database

    # Manage database (create/recreate)
    db_config = {
        'host': db_host,
        'port': int(db_port),
        'username': db_username,
        'password': db_password,
        'database': db_database
    }
    manage_database(db_config)

    # Run database migration
    print("Running database migration...")
    try:
        result = subprocess.run(
            ["uv", "run", "--project", "api", "flask", "db", "upgrade"],
            cwd="api",
            env=env,
            timeout=300
        )
        if result.returncode == 0:
            print("Database migration completed successfully")
        else:
            print(f"Migration failed with return code: {result.returncode}")
            exit(1)
    except subprocess.TimeoutExpired:
        print("Migration timed out")
        exit(1)
    except FileNotFoundError:
        print("uv command not found. Please ensure uv is installed")
        exit(1)