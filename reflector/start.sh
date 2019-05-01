mkdir -p /stream/${NAME}
rm -rf /stream/${NAME}/*

if test -n $YOUTUBE; then
	echo "Extracting m3u8 URI from YouTube link"
	echo "Youtube: "$YOUTUBE
	INPUT=$(youtube-dl -g $(echo $YOUTUBE))
	echo "m3u8 URI: "$INPUT
fi

echo "Starting ffmpeg ..."

/usr/bin/ffmpeg \
	-re \
	-i ${INPUT} \
	-bufsize 5000k \
	-vcodec copy -b:v 700k \
	-acodec copy \
	-hls_flags delete_segments \
	/stream/${NAME}/live.m3u8
