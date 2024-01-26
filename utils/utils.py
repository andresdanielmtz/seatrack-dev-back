import hashlib
import sqlite3
import os
import sys


def hash_password(password) -> str:
    """
    Hashes the given password using SHA-256 algorithm.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.

    """
    return hashlib.sha256(password.encode()).hexdigest()


# Route to establish a connection to the SQLite database
def get_coord_db_connection() -> sqlite3.Connection:
    root_path = os.getcwd()
    db_path = os.path.join(root_path, "coords.db")
    conn = sqlite3.connect(db_path)
    if conn is None:
        print("Error connecting to database.", file=sys.stderr)
    else:
        print("Connection established [coords.db]")

    conn.row_factory = sqlite3.Row
    return conn


def get_user_db_connection() -> sqlite3.Connection:
    root_path = os.getcwd()
    db_path = os.path.join(root_path, "userbase.db")
    conn = sqlite3.connect(db_path)
    if conn is None:
        print("Error connecting to database.", file=sys.stderr)
    else:
        print("Connection established [userbase.db]")
    conn.row_factory = sqlite3.Row
    return conn
