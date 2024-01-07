import hashlib
import sqlite3
import os


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Route to establish a connection to the SQLite database
def get_coord_db_connection(app):
    db_path = os.path.join(app.root_path, "coords.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_user_db_connection(app):
    db_path = os.path.join(app.root_path, "userbase.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
