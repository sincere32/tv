#!/bin/bash
docker kill tv-nginx
docker rm tv-nginx
docker build --rm -t tv/nginx:latest --squash .
docker image prune -f
docker run -d \
	--name tv-nginx \
	-p 30000:80 \
	-v stream:/tmp/stream \
	-v media:/tmp/media \
	--hostname=tv-nginx \
	tv/nginx
