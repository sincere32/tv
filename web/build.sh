#!/bin/bash
docker build --rm -t tv/web --squash .
#docker image prune -f
