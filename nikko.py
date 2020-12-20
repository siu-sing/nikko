from telethon.sync import TelegramClient
import telethon.sync
from telethon import functions, types
from time import sleep
import random

# app/account information
api_id = "2587653"
api_hash = "0229463569c8e0670949e36807d48798"
client = TelegramClient("a", api_id, api_hash)
client.start()
res = client.get_me().first_name
print("starting", res)
rn = random.randint(1,20)
print("sleep seconds", rn)
sleep(rn)
with open("./msg_templates/template_1","r") as msg_template:
    msg = msg_template.read()
client.send_message(-438471198, msg)
client.disconnect()
