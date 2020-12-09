#!/usr/bin/env python3

import connexion
from mongoengine import connect

from openapi_server import encoder
from openapi_server.config import Config

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', pythonic_params=True)

connect(
    db=Config().db_database,
    username=Config().db_username,
    password=Config().db_password,
    host=Config().db_host
)


def main():
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
