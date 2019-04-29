#!/bin/bash
docker build --rm -t tv/reflector:latest --squash .
#docker run --env "INPUT=http://www.radiosargentina.com.ar/php/tvm3u.php?id=DIAR0018" --env "NAME=france24" --name reflector tv/reflector
docker image prune -f
docker rm reflector
