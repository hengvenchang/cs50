import json
from channels import Channel
from channels.auth import channel_session_user_from_http, channel_session_user
from .models import Room
from .utils import get_room_or_error, catch_client_error
from .settings import MSG_TYPE_LEAVE, MSG_TYPE_ENTER, NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS
# This decorator copies the user from the HTTP session (only available in
# websocket.connect or http.request messages) to the channel session (available
# in all consumers with the same reply_channel, so all three here)
@channel_session_user_from_http
def ws_connect(message):
    print("connected")
    message.reply_channel.send({"accept": True})
    message.channel_session['rooms'] = []

def ws_receive(message):
    print("hello ws receive")
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.receive").send(payload)
    print("sent")

@channel_session_user
def chat_join(message):
    print(message["room"])
    room = get_room_or_error(message["room"], message.user)
    print("joined")
    if NOTIFY_USERS_ON_ENTER_OR_LEAVE_ROOMS:
        room.send_message(None, message.user, MSG_TYPE_ENTER)

    room.websocket_group.add(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(room.id),
            "title": room.title,
        }),
    })

@channel_session_user
def chat_send(message):
    if int(message['room']) not in message.channel_session['rooms']:
        print("error romm no exit")
    room = get_room_or_error(message["room"], message.user)
    room.send_message(message["message"], message.user)
