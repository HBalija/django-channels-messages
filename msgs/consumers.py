from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
import json

from .models import User, Message


@channel_session_user_from_http
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group('chat').add(message.reply_channel)


@channel_session_user
def ws_receive(message):

    user = User.objects.get(id=message.user.id)
    # save a new message
    msg = Message.objects.create(message=message.content['text'], user=user)

    # send message
    Group('chat').send({"text": json.dumps({
        'message': msg.message,
        'user': user.username
    })})


@channel_session_user
def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
