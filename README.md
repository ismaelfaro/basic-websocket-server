# basic-websocket-server
basic websocket server

## setup

> pip install -r requirements.txt

## run

> python server.py


# Docker image

## from Docker Hub

> docker run -p 8080:8080 ismaelfaro/websocket

## from local Dockerfile
### build image
> docker build --no-cache -t wsserver . 

### run container
> docker run -p 8080:8080 wsserver