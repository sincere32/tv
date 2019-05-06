$(document).ready(function () {

    is_menu_moving = false;
    beat = true;

    function menu_width() {
        var menu_width = $("#channel-list").width();
        return menu_width;
    }

    function hide_menu() {
        is_menu_moving = true;
        var width = menu_width();
        $("#channel-list").css("left", - menu_width)
        $("#channel-list").animate(
            {
                "left": - width
            },
            100,
            function () {
                is_menu_moving = false;
            }
        )
    }

    function show_menu() {
        is_menu_moving = true;
        $("#channel-list").animate(
            {
                "left": 0
            },
            100,
            function () {
                is_menu_moving = false;
            }
        )
    }

    $(document).mousemove(function (e) {
        var width = menu_width();
        var x = e.pageX;
        var y = e.pageY;
        if (!is_menu_moving) {
            if (x <= 0.3 * (width)) {
                show_menu();
            } else if (x > 1.2 * (width)) {
                hide_menu();
            }
        }

    });

    hide_menu();

    $(".channel-entry").on("click", function () {
        var video = videojs('player');
        var url = $(this).data("video-url").replace(" ", "-");
        console.log(url);
        video.src(url);
        video.play();
    });


});