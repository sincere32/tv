$(document).ready(function () {

    $(".channel-entry").on("click", function () {
        var video = videojs('player');
        var url = $(this).data("video-url").replace(" ","-");
        console.log(url);
        video.src(url);
        video.play();
    });

});