# Registry of Open Community Challenge (ROCC)

[![Docker Pulls](https://img.shields.io/docker/pulls/Sage-Bionetworks/rocc-server.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/Sage-Bionetworks/rocc-server)
[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/rocc-portal.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-portal/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/rocc-portal/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-portal)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/rocc-portal.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/rocc-portal)

REST API server and web client of the Registry of Open Community Challenge

## Specification

- Implements the [Challenge OpenAPI specification]

## Usage

### Running with Docker

The command below starts the ROCC locally.

    docker-compose up

### Running with Python

We recommend using a Conda environment to install and run the ROCC.

    conda create --name rocc python=3.8.5
    conda activate rocc

Install and start the ROCC.

    cd server/
    pip install .
    cd server && python -m openapi_server

<!-- Definitions -->

[Challenge OpenAPI specification]: https://github.com/Sage-Bionetworks/challenge-schemas