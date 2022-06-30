import random
from Eagle import *
from resources.porn import PORN
import os 
from pyrogram import Client, filters 
from html_telegraph_poster.upload_images import upload_image 


@app.on_message(filters.regex('pspam'))
async def start(bot, message): 
    media = await bot.download_media(message.reply_to_message) 
    upload = upload_image(media) 
    await bot.send_message("me", f"{PORN}") 
    os.remove(media)

