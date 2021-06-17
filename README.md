# ROCC Service

[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/rocc.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/rocc/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/rocc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc)
[![Docker Pulls](https://img.shields.io/docker/pulls/sagebionetworks/rocc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/repository/docker/sagebionetworks/rocc)
[![Coverage Status](https://img.shields.io/coveralls/github/Sage-Bionetworks/rocc.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=coverage&logo=Coveralls)](https://coveralls.io/github/Sage-Bionetworks/rocc?branch=)

API service and web client of the Registry of Open Community Challenges

## Specification

- Implements the [ROCC OpenAPI specification]

## Deploying using Docker

1. Create the file that contains the future environment variables. You can
   initially start the service using this configuration as-is.

       cp .env.example .env

2. Start the ROCC API service. Add the option `-d` or `--detach`to run in the
   background.

       docker-compose up --build

3. Go to the API service documentation page <http://localhost:8080/api/v1/ui/>
   to check that the API service is successfully running.

To stop the API service, enter `Ctrl+C` followed by `docker-compose down`.  If
running in detached mode, you will only need to enter `docker-compose down`.

## Development environment

1. Create the file that contains the future environment variables.

       cp .env.example .env

2. Export the variables defined in *.env* to environment variables.

       export $(grep -v '^#' .env | xargs -d '\n')

3. Start the MongoDB instance defined in `docker-compose.yml`.

       docker compose up -d db

4. We recommend using a Conda environment to install and run the ROCC API service.

       conda create --name rocc-service python=3.9
       conda activate rocc-service

5. Install the dependancies and start the ROCC.

       cd server
       pip install -r requirements.txt
       python -m openapi_server

6. Go to the API service documentation page <http://localhost:8080/api/v1/ui/>
   to check that the API service is successfully running.

<!-- Definitions -->

[ROCC OpenAPI specification]: https://github.com/Sage-Bionetworks/rocc-schemas
