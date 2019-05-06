mkdir -p /stream/${NAME}
rm -rf /stream/${NAME}/*
URI=$INPUT
echo $URI
/usr/bin/ffmpeg \
	-re \
	-i $URI \
	-bufsize 5000k \
	-vcodec copy -b:v 700k \
	-acodec copy \
	-hls_flags delete_segments \
	/stream/${NAME}/live.m3u8
