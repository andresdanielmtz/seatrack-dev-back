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
