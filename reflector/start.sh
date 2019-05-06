mkdir -p /stream/${NAME}
rm -rf /stream/${NAME}/*

/usr/bin/ffmpeg \
	-re \
	-i ${INPUT} \
	-bufsize 5000k \
	-vcodec copy -b:v 700k \
	-acodec copy \
	-hls_flags delete_segments \
	/stream/${NAME}/live.m3u8
