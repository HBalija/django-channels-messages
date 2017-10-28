from channels.routing import route, include
from msgs.consumers import ws_add, ws_disconnect, ws_receive

message_routing = [
    route("websocket.connect", ws_add),
    route('websocket.receive', ws_receive),
    route("websocket.disconnect", ws_disconnect),
]

channel_routing = [
    include(message_routing),
]
