# Inside utils/utils.py or any appropriate location

import sqlite3


def init_db():
    # Initialize coords.db
    conn_coords = sqlite3.connect("coords.db")
    conn_coords.execute(
        "CREATE TABLE IF NOT EXISTS Location (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, latitude REAL NOT NULL, longitude REAL NOT NULL)"
    )
    conn_coords.commit()
    conn_coords.close()

    # Initialize userbase.db
    conn_users = sqlite3.connect("userbase.db")
    conn_users.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)"
    )
    conn_users.commit()
    conn_users.close()
    

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
