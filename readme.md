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
After docker-compose up --build command succeeds docker desktop should display 3 running containers:
![image](https://github.com/user-attachments/assets/4d144935-92de-46f8-85e8-0339e3684447)
We can take a look into our consumer container and see that it is successfully validating messages:
![image](https://github.com/user-attachments/assets/13dcb9c9-266c-41fa-ba10-77a307f96977)
If we want to see events from the rabbitmq side we can visit: http://localhost:15672/
![image](https://github.com/user-attachments/assets/8aff9201-19d4-41ef-b1a5-48a7d0f4db5a)
We can see that our queue is actively getting messages published and we have one ip consuming (ours)
![image](https://github.com/user-attachments/assets/aee8a5a5-cc54-41ab-aab2-67f5164913cf)
Test Suite:
![image](https://github.com/user-attachments/assets/34731c62-7a5d-4ec4-a26e-af18c6e7bcca)

## Improvements
Since this code is meant to mock a distributed download monitoring system there are some improvments that could be made in a production setting:

- Credential handling (config files, environmental variables, internal auth system)
- Extend test suite based on biz logic and potential edge cases
- Centrally deploy rabbitmq rather than hosting alongside service
- Implement backend logic for succesful message events (hit api/db to notify to start import process etc)
- Implement production logging stack (hit elastic api / central logs resource)
- Improve error handling 



