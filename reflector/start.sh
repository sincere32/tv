mkdir -p /stream/${NAME}
rm -rf /stream/${NAME}/*

if ! [ -z $YOUTUBE_DL ]; then
	echo "Using youtube-dl extractor for " ${YOUTUBE_DL}
	INPUT=$(youtube-dl -g $YOUTUBE_DL)
fi

echo "URI is " ${INPUT}
echo "Starting FFMPEG ..."
echo ""
echo ""

/usr/bin/ffmpeg \
	-re \
	-i ${INPUT} \
	-bufsize 5000k \
	-vcodec copy -b:v 700k \
	-acodec copy \
	-hls_flags delete_segments \
	/stream/${NAME}/live.m3u8
