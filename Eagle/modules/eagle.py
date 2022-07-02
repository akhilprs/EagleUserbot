import os 
from pyrogram import Client, filters 
from Eagle import app
from html_telegraph_poster.upload_images import upload_image 


@app.on_message(filters.regex('.eagle'))
async def tm(bot, message):
    msg =  await bot.send_message(message.chat.id, "`Converting Telegraph To Telegraph Image!`")
    media = await bot.download_media(message.reply_to_message) 
    upload = upload_image(media) 
    await bot.edit_message(msg, f"Link:- {upload}") 
    os.remove(media)
