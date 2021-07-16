# ROCC API Service

[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/rocc-service.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-service/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/rocc-service/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-service)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/rocc-service.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-service)
[![Docker Pulls](https://img.shields.io/docker/pulls/sagebionetworks/rocc-service.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/repository/docker/sagebionetworks/rocc-service)
[![Coverage Status](https://img.shields.io/coveralls/github/Sage-Bionetworks/rocc-service.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=coverage&logo=Coveralls)](https://coveralls.io/github/Sage-Bionetworks/rocc-service?branch=)

## Introduction

This GitHub repository includes the code of the REST API service of the Registry
of Open Community Challenges (ROCC). This service implements the [ROCC OpenAPI
specification] (schemas).


## Specification

- ROCC schemas version: 0.1.7
- ROCC service version: 0.3.0
- Docker image: [sagebionetworks/rocc-service]


## Usage

### Running with Docker

Create the configuration file.

    cp .env.example .env

The command below starts the ROCC service locally.

    docker compose up --build

You can stop the container run with `Ctrl+C`, followed by `docker compose down`.

### Running with Python

We recommend using a Conda environment to install and run the ROCC service.

    conda create --name rocc-service python=3.9.4
    conda activate rocc-service

Create the configuration file and export its parameters to environment
variables.

    cp .env.example .env
    export $(grep -v '^#' .env | xargs -d '\n')

Start the MongoDB instance.

    docker compose up -d db

Install and start the ROCC service.

    cd server/
    pip install -r requirements.txt
    python -m openapi_server

### Acessing the Swagger UI

This API service provides a web interface (Swagger User Interface) that you can
use to interact with the service. The address of this interface depends on the
value of `SERVER_PORT` specified in `.env`.

- Swagger UI: `http://localhost:{SERVER_PORT}/ui`
- Swagger UI (default): http://localhost:8080/ui


## Versioning

### GitHub release tags

This repository uses [semantic versioning] to track the releases of this tool.
This repository uses "non-moving" GitHub tags, that is, a tag will always point
to the same git commit once it has been created.

### Docker image tags

The artifact published by the [CI/CD workflow] of this GitHub repository is a
Docker image pushed to the Docker Hub Registry. This table lists the image tags
pushed to the registry.

| Tag name                    | Moving | Description
|-----------------------------|--------|------------
| `latest`                    | Yes    | Latest stable release.
| `edge`                      | Yes    | Latest commit made to the default branch.
| `edge-<sha>`                | No     | Same as above with the reference to the git commit.
| `<major>.<minor>.<patch>`   | No     | Stable release.

You should avoid using a moving tag like `latest` when deploying containers in
production, because this makes it hard to track which version of the image is
running and hard to roll back.


## Contributing

Thinking about contributing to this project? Get started by reading our
[contribution guide].


## License

[Apache License 2.0]

<!-- Links -->

[sagebionetworks/rocc-service]: https://hub.docker.com/repository/docker/sagebionetworks/rocc-service
[ROCC OpenAPI specification]: https://github.com/Sage-Bionetworks/rocc-schemas
[semantic versioning]: https://semver.org/
[CI/CD workflow]: .github/workflows/ci.yml
[contribution guide]: .github/CONTRIBUTING.md
[Apache License 2.0]: https://github.com/Sage-Bionetworks/rocc/blob/main/LICENSE
