from flask import Blueprint
import sqlite3

profile_blueprint = Blueprint("profile", __name__)


@profile_blueprint.route("/profile")
def profile():
    response_body = {
        "name": "Andres Martinez",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
    }

    return response_body


@profile_blueprint.route("/profile/coords")
def profile_coords():
    conn = sqlite3.connect("coords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Location")
    rows = cursor.fetchall()
    conn.close()
    response_body = []
    for row in rows:
        response_body.append(
            {"id": row[0], "name": row[1], "latitude": row[2], "longitude": row[3]}
        )
    return {"coords": response_body}
