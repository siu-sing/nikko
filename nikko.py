from telethon.sync import TelegramClient
import telethon.sync
from telethon import functions, types
from time import sleep
import random
import json
import config as cfg
from datetime import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: python nikko.py <freq>")
    sys.exit()


def send_message(job_name, api_id, api_hash, msg_file, recipients):

    # Start TG Client
    client = TelegramClient(job_name, api_id, api_hash)
    client.start()
    username = client.get_me().first_name

    # Pause for random amount of time
    sleep(random.randint(1, 20))

    # Read in message template
    with open(f"./msg_templates/{msg_file}", "r") as msg_template:
        msg = msg_template.read()

    # Broadcast messages to all recipients one by one
    for r in recipients:
        try:
            client.send_message(r, msg)
            print(
                f"{datetime.now()} : INFO: Message sent from {username} to {r} with {msg_file}"
            )
        except Exception as e:
            print(
                f"{datetime.now()} : FAILED: Unable to send from {username} to {r} with {msg_file}"
            )
            print(f"ERROR: {e}")

    client.disconnect()


freq = sys.argv[1]
for j in cfg.jobs[freq]:
    send_message(
        j["job_name"], j["api_id"], j["api_hash"], j["msg_file"], j["recipients"]
    )
