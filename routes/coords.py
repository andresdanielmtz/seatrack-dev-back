from flask import jsonify, request, Blueprint, current_app
from utils.utils import get_coord_db_connection
import sys

coords_blueprint = Blueprint("coords", __name__)


@coords_blueprint.route("/coords", methods=["GET", "POST"])
def coords():
    conn = get_coord_db_connection(current_app)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Location")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))

    conn.close()

    return jsonify(result)  # Return JSON response


@coords_blueprint.route("/register_coord", methods=["POST"])
def register_coord():
    lat = request.json.get("latitude")
    lng = request.json.get("longitude")
    name = request.json.get("name")

    conn = get_coord_db_connection(current_app)
    cursor = conn.cursor()

    print(f"REGISTERING: {lat}, {lng}, {name}", file=sys.stderr)
    cursor.execute(
        "INSERT INTO Location (name, latitude, longitude) VALUES (?, ?, ?)",
        (name, lat, lng),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Registration Complete!"})
