#!/usr/bin/env python3

import connexion
import flask
from flask_cors import CORS
from flask_login import LoginManager, current_user
from mongoengine import connect
from oauthlib.oauth2 import WebApplicationClient
import requests

from openapi_server import encoder
from openapi_server.config import config

app = connexion.App(__name__, specification_dir="./openapi/")
app.app.json_encoder = encoder.JSONEncoder
app.add_api("openapi.yaml", pythonic_params=True)

# Additional routes
app.add_url_rule("/ui", "ui", lambda: flask.redirect("/api/v1/ui"))

# Add CORS support
# https://connexion.readthedocs.io/en/latest/cookbook.html#cors-support
CORS(app.app, resources={r"/api/*": {"origins": "*"}})

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app.app)

# Database setup
connect(
    db=config.db_database,
    username=config.db_username,
    password=config.db_password,
    host=config.db_host,
)

# OAuth 2 client setup
print(f"Google Client ID: {config.google_client_id}")
client = WebApplicationClient(config.google_client_id)

print(f"Server secret key: {config.secret_key}")


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return ""  # User.get(user_id)


@app.route("/home")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'


def get_google_provider_cfg():
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        # redirect_uri=flask.request.base_url + "/callback",
        redirect_uri="https://localhost:8080/api/v1/auth/googleOAuth/callback",
        scope=["openid", "email", "profile"],
    )
    return flask.redirect(request_uri)


def main():
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
