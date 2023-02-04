import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5786986338:AAFZk_J25RrHeRtTPQ5-L_zsgthVJK88X1g")

API_ID = int(os.environ.get("API_ID", "5503927"))

API_HASH = os.environ.get("API_HASH", "6f3a051b5da7f5b499cde019d273fca1")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
