from telethon.sync import TelegramClient
import telethon.sync
from telethon import functions, types
from datetime import datetime
import sys

if (len(sys.argv)<4):
  print("Usage: python register_user.py <job_name> <api_id> <api_hash>")
  sys.exit()  


job_name = sys.argv[1]
api_id = sys.argv[2]
api_hash = sys.argv[3]

client = TelegramClient(job_name, api_id, api_hash)
client.start()
username = client.get_me().first_name

print(f"{username} registered.")

client.disconnect()