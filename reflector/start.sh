rm -rf /stream/${NAME}
mkdir -p /stream/${NAME}

if ! [ -z $YOUTUBE_DL ]; then
	echo "Using youtube-dl extractor for " ${YOUTUBE_DL}
	INPUT=$(youtube-dl -g $YOUTUBE_DL)
fi

echo "URI is " ${INPUT}
echo "Starting FFMPEG ..."
echo "Codec options are :"
echo ${VCODEC}
echo ""
echo ""

/usr/bin/ffmpeg \
	-re \
	-i ${INPUT} \
	-bufsize 5000k \
	-vcodec ${VCODEC} \
	-acodec aac \
	-hls_flags delete_segments \
	/stream/${NAME}/live.m3u8

rm -rf /stream/${NAME}
