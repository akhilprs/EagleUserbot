import os 
from pyrogram import Client, filters 
from Eagle import app
from html_telegraph_poster.upload_images import upload_image 


@app.on_message(filters.regex('.eagle'))
async def start(bot, message): 
    media = await bot.download_media(message.reply_to_message) 
    upload = upload_image(media) 
    await bot.send_message("me", f"Link:- https://te.legra.ph/file/543a358625382cc27fd2b.jpg") 
    os.remove(media)
