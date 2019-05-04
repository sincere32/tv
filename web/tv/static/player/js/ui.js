$(document).ready(function () {

    function menu_width() {
        var menu_width = $("#channel-list").width();
        return menu_width;
    }
    function hide_menu() {
        var menu_width = $("#channel-list").width();
        $("#channel-list").css("left", -menu_width)
    }
    function show_menu() {
        $("#channel-list").css("left", 0)
    }
    hide_menu();

    $(".channel-entry").on("click", function () {
        var video = videojs('player');
        var url = $(this).data("video-url").replace(" ", "-");
        console.log(url);
        video.src(url);
        video.play();
    });

    $(document).mousemove(function (e) {
        var width = menu_width();
        var x = e.pageX;
        var y = e.pageY;
        if(x<=width) {
            show_menu();
        } else {
            hide_menu();
        }
        console.log(x);
    });
});