$(document).ready(function () {


    var socket = io();
    socket.on('score1', function (msg, cb) {
        console.log("Player one's score: " + msg.player_one_score);
        $('#scoreone').animate({
            opacity: 0,
        }, 300);
        setTimeout(() => {
            $('#scoreone').text(msg.player_one_score);
        }, "300");
        $('#scoreone').animate({
            opacity: 1,
        }, 300);

        if (cb)
            cb();
    });

    socket.on('score2', function (msg, cb) {
        console.log("Player two's score: " + msg.player_two_score)
        $('#scoretwo').animate({
            opacity: 0,
        }, 300);
        setTimeout(() => {
            $('#scoretwo').text(msg.player_two_score);
        }, "300");

        $('#scoretwo').animate({
            opacity: 1,
        }, 300);

        if (cb)
            cb();
    });

    // When JS recieves "Fadeout" from python, start fading out
    socket.on('fadeout', function (msg, cb) {
        console.log("Fading out")

        $('.container').animate({
            opacity: 0,
        }, 300);

        if (cb)
            cb();
    });

    function fadein() {
        // Makes container invisible on page load.
        $('.container').animate({
            opacity: 0,
        }, 0);
        // After # of milliseconds, start animation for fade in.
        setTimeout(() => {
            $('.container').animate({
                opacity: 1,
            }, 300);
        }, "300");
        console.log("Fading in");
    };

    fadein()

    socket.on('reset', function (msg, cb) {
        console.log("Resetting.");
    });

    socket.on('fadein', function (msg, cb) {
        fadein()
    });

    window.scoreup1 = function () {
        socket.emit("scoreup1");
    };

    window.scoredown1 = function () {
        socket.emit("scoredown1")
    }

    window.scoreup2 = function () {
        socket.emit("scoreup2");
    };

    window.scoredown2 = function () {
        socket.emit("scoredown2")
    }

    window.hide = function () {
        socket.emit("hide");
    };

    window.reload = function () {
        socket.emit("reset");
    }

    window.fadein = function () {
        socket.emit("fadein");
    }

    window.fullreset = function () {
        socket.emit("hide");
        socket.emit("reset");
    }
});

