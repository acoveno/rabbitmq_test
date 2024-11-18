# RabbitMQ Download Monitor

A distributed system for monitoring download events using RabbitMQ message queues.

## Features
- Producer generates simulated download events with coordinates, file size, and speed
- Consumer validates events against JSON schema
- Invalid messages are redirected to a reject queue
- Containerized with Docker and Docker Compose
- Test suite using pytest

## Requirements
- Docker
- Docker Compose

## Setup & Running
1. Start services:

docker-compose up --build

2. Run tests:

docker-compose run consumer pytest

OR

docker-compose run producer pytest

## Output
TODO
