from pytg.sender import Sender
from pytg.receiver import Receiver
from pytg.utils import coroutine
from time import sleep
from requests.exceptions import ConnectionError

adapter_config = {
    "name": "telegram",
    "blocked_users_id": [],
    "admin_ids": [
        "user#23897509"
    ]
}

telegram_sender = Sender(host="localhost", port=4458)
telegram_receiver = Receiver(host="localhost", port=4458)
message = {}


@coroutine
def parse_telegram_messages():
    global message
    msg = (yield)
    message = {
        'text': msg['text'],
        'time': msg['date'],
        'sender_id': msg['sender']['cmd'],
        'sender_type': msg['sender']['type'],
        'user_id': msg['sender']['cmd']
    }
    return message


def get_messages():
    global message
    telegram_receiver.start()
    try:
        telegram_receiver.message(
            parse_telegram_messages()
        )
    except KeyboardInterrupt:
        telegram_receiver.stop()
        exit()
    return [message]


def send_message(sender_id, sender_type,
                 message_text="", message_photos=[]):
    print(message_text, message_photos, sender_id, sender_type)
    return True
