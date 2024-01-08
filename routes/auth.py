from flask import session, jsonify, request, Blueprint, current_app
from utils.utils import get_user_db_connection, hash_password
import sys

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    print("LOGGING IN: ", username, file=sys.stderr)
    try:
        conn = get_user_db_connection()
        cursor = conn.cursor()

        # Retrieve the hashed password for the provided username
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        stored_password = cursor.fetchone()

        if stored_password:
            stored_password = stored_password["password"]

            # Compare hashed passwords
            if stored_password == hash_password(password):
                session["logged_in"] = True
                session["username"] = username
                response = {"message": "Login successful", "status": 200}
            else:
                response = {"message": "Invalid Credentials", "status": 401}
        else:
            response = {"message": "Invalid Credentials", "status": 401}

    except Exception as e:
        print(f"Error connecting to database: {e}", file=sys.stderr)
        response = {"message": "Internal Server Error", "status": 500}

    finally:
        if conn:
            conn.close()

    print(f"LOGIN: {response['message']}", file=sys.stderr)
    return jsonify(response), response["status"]


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})


@auth_blueprint.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    conn = get_user_db_connection()
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        return jsonify({"message": "Username already exists"}), 409

    # Hash the password before storing it
    hashed_password = hash_password(password)

    print(f"REGISTERING: {username}, {hashed_password}", file=sys.stderr)
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Registration Complete!"})
