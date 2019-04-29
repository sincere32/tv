FROM alpine
MAINTAINER Arturo Baldo <baldoarturo@gmail.com>

RUN apk upgrade -U \
 && apk add ca-certificates ffmpeg libva-intel-driver \
 && rm -rf /var/cache/*

WORKDIR /stream/
COPY ./start.sh /stream/start.sh
RUN chmod +x /stream/start.sh
CMD /stream/start.sh
