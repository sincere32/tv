#!/bin/bash
docker rm tv-nginx
docker build --rm -t tv/nginx:latest --squash .
docker image prune -f
docker run -d --name tv-nginx -p 30000:80 -v stream:/usr/share/nginx/html/stream  tv/nginx
