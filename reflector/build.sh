#!/bin/bash
docker build --rm -t tv/reflector:latest .
docker image prune -f
