$(document).ready(function(){
    var video = videojs('player');
    var url = 'http://192.168.15.253:30000/stream/canal26/live.m3u8';
    video.src(url);
    video.play();
});