import random
from Eagle import *
from resources.porn import PORN
import os 
from pyrogram import Client, filters 

@app.on_message(filters.command("pspam", PREFIX) & filters.me)
async def pspam(bot, message): 
    media = resources.porn import PORN  
    upload = upload_image 
    await bot.send_message("me", f"{PORN}") 
    os.remove(media)

