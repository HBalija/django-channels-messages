$(document).ready(function () { // eslint-disable-line
    var wsScheme = window.location.protocol === "https:" ? "wss" : "ws";

    // messaging socket
    var socketMessage = new WebSocket(wsScheme + "://" + window.location.host + "/");

    $("#formButtonId").click(function(event) { // eslint-disable-line
        event.preventDefault();
        // don't send if area empty
        if (!$('#id_message').val()) {
            return;
        }
        // sending message
        socketMessage.send($('#id_message').val());
        // clearing textarea
        $('#id_message').val('');
    });

    socketMessage.onmessage = function (e) {  // eslint-disable-line
        var data = JSON.parse(e.data);
        var msgRow = "<li><strong>" + data.user + "</strong>: " + data.message + "</li>";

        $("ul").find(".messages-list").append(msgRow);
    };

    $("#id_message").keydown(function (event) {  // eslint-disable-line
        if (event.keyCode === 13 && !event.shiftKey) {
            event.preventDefault();
            $("#formButtonId").click();
        }
    });
});
