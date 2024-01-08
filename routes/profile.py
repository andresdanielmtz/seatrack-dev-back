from flask import Blueprint, jsonify, current_app
from utils.utils import get_coord_db_connection, get_user_db_connection

profile_blueprint = Blueprint("profile", __name__)


@profile_blueprint.route("/")
def index():
    return "Hello World!"


@profile_blueprint.route("/profile")
def profile():
    response_body = {
        "name": "Andres Martinez",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
    }

    return response_body


@profile_blueprint.route("/profile/coords")
def profile_coords():
    conn = get_coord_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Location")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))

    conn.close()

    return jsonify(result)  # Return JSON response


@profile_blueprint.route("/profile/userbase")
def profile_userbase():
    conn = get_user_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))

    conn.close()

    return jsonify(result)  # Return JSON response
