mkdir -p /stream/${NAME}
<<<<<<< HEAD
rm -rf /stream/${NAME}/*

/usr/bin/ffmpeg \
	-re \
	-i ${INPUT} \
	-bufsize 5000k \
	-vcodec copy -b:v 700k \
	-acodec copy \
	-hls_flags delete_segments \
	/stream/${NAME}/live.m3u8
=======
/usr/bin/ffmpeg -re -i ${INPUT} \
    -bufsize 5000k \
    -vcodec copy -b:v 1000k \
    -acodec copy \
    -hls_flags delete_segments \
    "'/stream/'"${NAME}"'/live.m3u8'"
>>>>>>> 9936e7199dc59ae6fe68aafbae96f3cf4fa0aefd
