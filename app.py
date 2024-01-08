from flask import Flask
from flask_cors import CORS
from flask_session import Session
import os
import sqlite3

from routes.auth import auth_blueprint
from routes.coords import coords_blueprint
from routes.profile import profile_blueprint

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SESSION_TYPE"] = "filesystem"
app.config.from_object(__name__)
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_PERMANENT"] = True  # Make the session cookie persistent
app.config["PERMANENT_SESSION_LIFETIME"] = (
    3600 * 24 * 7
)  # Set the lifetime to 1 week (adjust as needed)
app.config["COORDS_DATABASE"] = os.path.join(app.root_path, "coords.db")
app.config["USERBASE_DATABASE"] = os.path.join(app.root_path, "userbase.db")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")


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


init_db()

CORS(app, supports_credentials=True)
Session(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(coords_blueprint)
app.register_blueprint(profile_blueprint)

SESSION_TYPE = "redis"

if __name__ == "__main__":
    with app.app_context():
        app.run(port=9000, debug=True)
