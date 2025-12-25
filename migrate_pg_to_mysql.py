#!/usr/bin/env python3
"""
Dify Plugin Daemon 数据迁移脚本 (PostgreSQL → MySQL)

这个脚本使用 SQLAlchemy Core 和 Table Reflection 自动发现表结构，
无需手动定义模型，直接迁移所有数据。

特性:
    - 自动发现 PostgreSQL 表结构
    - 自动创建 MySQL 表结构
    - 保留 created_at 和 updated_at 时间戳
    - 批量插入提高性能
    - 事务保护
"""

import os
import sys
from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, select, insert, inspect
from sqlalchemy.exc import OperationalError

# 默认配置
DEFAULT_PG_HOST = "localhost"
DEFAULT_PG_PORT = 5432
DEFAULT_PG_DB = "dify_plugin"
DEFAULT_PG_USER = "postgres"
DEFAULT_PG_PASSWORD = "difyai123456"

DEFAULT_MYSQL_HOST = "localhost"
DEFAULT_MYSQL_PORT = 3306
DEFAULT_MYSQL_DB = "dify_plugin"
DEFAULT_MYSQL_USER = "root"
DEFAULT_MYSQL_PASSWORD = "difyai123456"

BATCH_SIZE = 100


def get_env(key, default):
    """获取环境变量"""
    return os.environ.get(key, default)


def create_pg_engine():
    """创建 PostgreSQL 连接"""
    pg_url = f"postgresql://{get_env('PG_USER', DEFAULT_PG_USER)}:{get_env('PG_PASSWORD', DEFAULT_PG_PASSWORD)}@{get_env('PG_HOST', DEFAULT_PG_HOST)}:{get_env('PG_PORT', DEFAULT_PG_PORT)}/{get_env('PG_DB', DEFAULT_PG_DB)}"
    return create_engine(pg_url)


def create_mysql_engine():
    """创建 MySQL 连接"""
    mysql_url = f"mysql+pymysql://{get_env('MYSQL_USER', DEFAULT_MYSQL_USER)}:{get_env('MYSQL_PASSWORD', DEFAULT_MYSQL_PASSWORD)}@{get_env('MYSQL_HOST', DEFAULT_MYSQL_HOST)}:{get_env('MYSQL_PORT', DEFAULT_MYSQL_PORT)}/{get_env('MYSQL_DB', DEFAULT_MYSQL_DB)}?charset=utf8mb4"
    return create_engine(mysql_url)


def migrate_table(pg_engine, mysql_engine, table_name, current, total):
    """迁移单个表的数据"""
    print(f"[{current}/{total}] 迁移 {table_name:<40}", end=" ")
    
    # 反射表结构
    pg_metadata = MetaData()
    pg_table = Table(table_name, pg_metadata, autoload_with=pg_engine)
    
    mysql_metadata = MetaData()
    mysql_table = Table(table_name, mysql_metadata, autoload_with=mysql_engine)
    
    # 读取 PostgreSQL 数据
    with pg_engine.connect() as pg_conn:
        result = pg_conn.execute(select(pg_table))
        rows = result.fetchall()
        
        if not rows:
            print("   0 条记录（跳过）")
            return 0
        
        # 批量写入 MySQL
        with mysql_engine.begin() as mysql_conn:
            for i in range(0, len(rows), BATCH_SIZE):
                batch = rows[i:i + BATCH_SIZE]
                
                # 转换为字典列表
                batch_dicts = []
                for row in batch:
                    row_dict = dict(row._mapping)
                    batch_dicts.append(row_dict)
                
                # 插入数据（保留时间戳）
                mysql_conn.execute(insert(mysql_table), batch_dicts)
        
        print(f"   {len(rows)} 条记录 ✓")
        return len(rows)


def main():
    print("╔══════════════════════════════════════════════════════════════════════════╗")
    print("║       Dify Plugin Daemon 数据迁移工具 (PostgreSQL → MySQL)              ║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")
    print()
    
    # Step 1: 连接 PostgreSQL
    print("📡 正在连接 PostgreSQL...")
    try:
        pg_engine = create_pg_engine()
        with pg_engine.connect() as conn:
            conn.execute(select(1))
        print("✅ PostgreSQL 连接成功")
    except OperationalError as e:
        print(f"❌ PostgreSQL 连接失败: {e}")
        sys.exit(1)
    print()
    
    # Step 2: 连接 MySQL
    print("📡 正在连接 MySQL...")
    try:
        mysql_engine = create_mysql_engine()
        with mysql_engine.connect() as conn:
            conn.execute(select(1))
        print("✅ MySQL 连接成功")
    except OperationalError as e:
        print(f"❌ MySQL 连接失败: {e}")
        sys.exit(1)
    print()
    
    # Step 3: 验证 MySQL 表是否存在
    print("🔍 检查 MySQL 表结构...")
    inspector = inspect(mysql_engine)
    mysql_tables = inspector.get_table_names()
    if not mysql_tables:
        print("❌ MySQL 中没有表，请先创建表结构")
        print("   提示: 修改 dify-plugin-daemon 的 .env 设置 DB_TYPE=mysql，启动一次服务即可自动创建表")
        sys.exit(1)
    print(f"✅ 发现 {len(mysql_tables)} 张表")
    print()
    
    # Step 4: 获取所有表名
    inspector = inspect(pg_engine)
    table_names = inspector.get_table_names()
    
    print(f"🚀 开始迁移数据...")
    print("═══════════════════════════════════════════════════════════════════════════")
    print()
    
    # Step 5: 迁移每个表
    total_records = 0
    start_time = datetime.now()
    
    for i, table_name in enumerate(sorted(table_names), 1):
        try:
            count = migrate_table(pg_engine, mysql_engine, table_name, i, len(table_names))
            total_records += count
        except Exception as e:
            print(f"❌ 迁移表 {table_name} 失败: {e}")
            sys.exit(1)
    
    duration = datetime.now() - start_time
    
    # Summary
    print()
    print("═══════════════════════════════════════════════════════════════════════════")
    print("✅✅✅ 所有数据迁移完成！")
    print()
    print(f"   总表数: {len(table_names)}")
    print(f"   总记录数: {total_records}")
    print(f"   耗时: {duration}")
    print()
    print("💡 提示：")
    print("   1. 建议验证数据完整性（检查记录数和时间戳）")
    print("   2. 修改 .env 文件的 DB_TYPE=mysql 切换到 MySQL")
    print("   3. 重启 dify-plugin-daemon 服务")
    print("═══════════════════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()

