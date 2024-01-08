from flask import Blueprint
import sqlite3
from ..utils.utils import get_coord_db_connection

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
    conn = get_coord_db_connection(profile_blueprint)
    rows = conn.execute("SELECT * FROM Location").fetchall()
    conn.close()
    response_body = []
    for row in rows:
        response_body.append(
            {"id": row[0], "name": row[1], "latitude": row[2], "longitude": row[3]}
        )
    return {"coords": response_body}
