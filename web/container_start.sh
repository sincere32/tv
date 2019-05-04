#!/bin/sh
docker kill tv-web
docker rm tv-web
docker run -d \
	--name tv-web \
	--hostname=tv-web \
        -v stream:/tmp/stream \
        -v media:/django/media \
	tv/web
