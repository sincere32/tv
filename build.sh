#!/bin/bash
sh reflector/build.sh
docker volume create --name=tv-streams
docker volume create --name=tv-web-media
docker volume create --name=tv-database
docker-compose build
docker-compose up -d
