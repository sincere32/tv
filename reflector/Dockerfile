FROM alpine
MAINTAINER Arturo Baldo <baldoarturo@gmail.com>

RUN apk upgrade -U \
 && apk add ca-certificates ffmpeg libva-intel-driver \
 && rm -rf /var/cache/*

WORKDIR /
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
CMD /start.sh
