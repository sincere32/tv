mkdir -p /stream/${NAME}
/usr/bin/ffmpeg -re -i ${INPUT} \
    -bufsize 5000k \
    -vcodec copy -b:v 1000k \
    -acodec copy \
    -hls_flags delete_segments \
    "'/stream/'"${NAME}"'/live.m3u8'"
