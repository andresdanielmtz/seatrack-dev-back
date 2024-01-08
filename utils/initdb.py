# Inside utils/utils.py or any appropriate location

import sqlite3


def create_table_from_sql(conn, sql_file_path):
    # Execute SQL statements from the specified file
    with open(sql_file_path, "r") as sql_file:
        sql_statements = sql_file.read()
        conn.executescript(sql_statements)


def does_table_exist(conn, table_name):
    # Check if the table exists in the database
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    result = conn.execute(query).fetchone()
    return result is not None
