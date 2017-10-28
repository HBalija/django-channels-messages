$(document).ready(function () { // eslint-disable-line

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

    // messaging socket
    socket_message = new WebSocket(ws_scheme + "://" + window.location.host + "/");
    $("#formButtonId").click(function(event)  {
        event.preventDefault(); // cancel default behavior
        if (!$('#id_message').val()) return;
        socket_message.send($('#id_message').val())
        $('#id_message').val('');
    });

    var $scrollDiv = $(".js-scroll-bar");

    // check if message exists (if not, message table is hidden)
    if($scrollDiv.attr("data-msg") === "[]") {
        $scrollDiv.hide();
    }

    socket_message.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var msgRow = "<tr><td>" + data.user + "</td><td>" + data.message + "</td></tr>"

        $("table").find("tbody").append(msgRow)

        // show message table
        $scrollDiv.show();

        scroll_div.scrollTop = scroll_div.scrollHeight;
    }

    var scroll_div = document.getElementById("scroll_bottom");
    if (scroll_div) {
        scroll_div.scrollTop = scroll_div.scrollHeight;
    }

});
