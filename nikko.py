from telethon.sync import TelegramClient
import telethon.sync
from telethon import functions, types
from time import sleep
import random
import json
import config as cfg
from datetime import datetime

def send_message(job_name, api_id, api_hash, msg_file, recipients):
    
    # Start TG Client
    client = TelegramClient(job_name, api_id, api_hash)
    client.start()
    username = client.get_me().first_name

    # Pause for random amount of time    
    sleep(random.randint(1,20))
    
    # Read in message template
    with open(f"./msg_templates/{msg_file}","r") as msg_template:
        msg = msg_template.read()

    # Broadcast messages to all recipients one by one
    for r in recipients: 
        client.send_message(r, msg)
        print(f"{datetime.now()} : INFO: Message sent from {username} to {r} with {msg_file}")

    client.disconnect()
    
for j in cfg.jobs:
    send_message(j["job_name"], j["api_id"], j["api_hash"],j["msg_file"], j["recipients"])
    

