from flask import Blueprint

profile_blueprint = Blueprint("profile", __name__)


@profile_blueprint.route("/profile")
def profile():
    response_body = {
        "name": "Andres Martinez",
        "about": "Hello! I'm a full stack developer that loves python and javascript",
    }

    return response_body
