#!/usr/bin/env python3

import connexion

from openapi_server import encoder

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'ROCC API'},
            pythonic_params=True)


def main():
    # TODO: Consider using param host="0.0.0.0", debug=True,
    app.run(port=8080)


if __name__ == '__main__':
    main()
