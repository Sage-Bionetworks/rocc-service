#!/usr/bin/env python3

import json
import connexion
import flask
from flask_cors import CORS
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin,
)
from mongoengine import connect
from oauthlib.oauth2 import WebApplicationClient
import requests

from openapi_server import encoder
from openapi_server.config import config


class User(UserMixin):
    def __init__(self, id, active=True):
        self.id = id
        self.active = active

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


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
print(f"Google Client secret: {config.google_client_secret}")
client = WebApplicationClient(config.google_client_id)

print(f"Server secret key: {config.secret_key}")
app.app.secret_key = config.secret_key

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User(id="12345")  # User.get(user_id)


@app.route("/home")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                # current_user.name, current_user.email, current_user.profile_pic
                "dummy_name",
                "dummy_email",
                "dummy_profile_pic",
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
        redirect_uri="https://localhost:8080/login/callback",
        scope=["openid", "email", "profile"],
    )
    return flask.redirect(request_uri)


@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = flask.request.args.get("code")
    print(f"code: {code}")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=flask.request.url,
        redirect_url=flask.request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(config.google_client_id, config.google_client_secret),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        print(f"unique_id: {unique_id}")
        print(f"users_email: {users_email}")
        print(f"picture: {picture}")
        print(f"users_name: {users_name}")
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided
    # by Google
    # user = User(
    #     id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    # )
    user = User(id=unique_id)

    # Doesn't exist? Add it to the database.
    # if not User.get(unique_id):
    #     User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return flask.redirect(flask.url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for("index"))


def main():
    app.run(port=8080, debug=True, ssl_context="adhoc")
    flask.session.clear()


if __name__ == "__main__":
    main()
