from flask import Flask
from flask_cors import CORS
from flask_session import Session
import os

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


CORS(app)
Session(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(coords_blueprint)
app.register_blueprint(profile_blueprint)

SESSION_TYPE = "redis"

if __name__ == "__main__":
    with app.app_context():
        app.run(port=5000, debug=True)
