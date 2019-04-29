mkdir -p /stream/${NAME}
/usr/bin/ffmpeg -re -i ${INPUT} -vcodec copy -acodec copy -hls_flags delete_segments /stream/${NAME}/live.m3u8
