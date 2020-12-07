# Registry of Open Community Challenge (ROCC)

[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/rocc-portal.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-portal/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/rocc-portal/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-portal)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/rocc-portal.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-portal)
[![Docker Pulls](https://img.shields.io/docker/pulls/sagebionetworks/rocc-server.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/repository/docker/sagebionetworks/rocc-server)

API and web client of the Registry of Open Community Challenge

## Specification

- Implements the [Challenge OpenAPI specification]

## Deploying using Docker

1. Create the file that contains the future environment variables

       cp .env.sample .env

2. Export the variables defined in *.env* to environment variables

       export $(grep -v '^#' .env | xargs -d '\n')

3. Start the Data Node API service

       docker-compose up

4. In your browser, go to the API service documentation page
   <http://localhost:8080/api/v1/ui/> to check that the API service is
   successfully running.

## Running with Python

We recommend using a Conda environment to install and run the ROCC.

    conda create --name rocc python=3.8.5
    conda activate rocc

Install and start the ROCC.

    cd server/
    pip install .
    cd server && python -m openapi_server

<!-- Definitions -->

[Challenge OpenAPI specification]: https://github.com/Sage-Bionetworks/challenge-schemas