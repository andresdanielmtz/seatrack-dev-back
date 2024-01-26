from flask import session, jsonify, request, Blueprint, current_app
from utils.utils import get_user_db_connection, hash_password
from utils.auth import valid_email
import sys

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/check", methods=["GET"])
def check() -> tuple:
    if session.get("logged_in"):
        return jsonify({"message": "Logged in"})
    else:
        return jsonify({"message": "Not logged in"})


@auth_blueprint.route("/login", methods=["POST"])
def login() -> tuple:
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")
    print("LOGGING IN: ", username, "\n", password, file=sys.stderr)
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
                session["email"] = email
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
def logout() -> tuple:
    session.clear()
    return jsonify({"message": "Logged out"})


@auth_blueprint.route("/register", methods=["POST"])
def register() -> tuple:
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")

    # Check if username or password is empty
    if not username or not password:
        return jsonify({"message": "Username or password is empty"}), 400

    # Check if email is valid
    if not valid_email(email):
        return jsonify({"message": "Invalid email"}), 400

    conn = get_user_db_connection()
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        return jsonify({"message": "Username already exists"}), 409

    # Hash the password before storing it
    hashed_password = hash_password(password)

    print(f"REGISTERING: {username}, {hashed_password}, {email}", file=sys.stderr)
    cursor.execute(
        "INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
        (email, username, hashed_password),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Registration Complete!"})
