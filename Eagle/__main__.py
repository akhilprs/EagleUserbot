from pyrogram import idle, Client, filters
from config import PREFIX
from Eagle import app, LOGGER
import logging
from Eagle.modules import *
import uvloop

uvloop.install() # speedup

app.start()
me = app.get_me()
print(f"Your Eagle Userbot is ready to fly... Congratulations {me.id} !!. Type {PREFIX}alive to check If your bot is working... Join @EAGLEUB for future updates...")
idle()
