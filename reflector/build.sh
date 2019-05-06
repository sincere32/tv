#!/bin/bash
docker build --rm -t tv/reflector:latest --squash .
docker image prune -f
