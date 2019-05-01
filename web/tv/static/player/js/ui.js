$(document).ready(function() {
    var video = videojs('player');
    var url = 'http://localhost:30000/stream/tn/live.m3u8';
    video.src(url);
    video.play();
});