import os 
from pyrogram import Client, filters 
from Eagle import app
from html_telegraph_poster.upload_images import upload_image 


@app.on_message(filters.regex('.telegraph'))
async def tm(bot, message):
    await bot.edit_message_text(message.chat.id, message.id, "`Converting Image To Telegraph!`")
    media = await bot.download_media(message.reply_to_message) 
    upload = upload_image(media) 
    await bot.edit_message_text(message.chat.id, message.id, f"Link:- {upload}") 
    os.remove(media)
