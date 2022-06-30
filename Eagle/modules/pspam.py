# import asyncio
# import random
# from Eagle import *
# from resources.porn import PORN
# import os 
# from pyrogram import Client, filters 
# from Eagle import app, CMD_HELP
# from config import PREFIX

# CMD_HELP.update(
#    {
#        "Porn Spam": """
#🦅 **Porn Spam** 🦅
#  `pspam` ~ Spam 18+ GIF/ Videos, 18+ Don't use this, not made for kids 🙂.  
# """
 #   }
# )

# que = {}

# global que
#    queue = que.get(event.sender_id)
#    if not queue:
 #       return
 #   async with event.client.action(event.chat_id, "typing"):
#        await asyncio.sleep(0.4)
#    async with event.client.action(event.chat_id, "typing"):
#        await asyncio.sleep(1)
 #       await event.client.send_message(
 #           entity=event.chat_id,
 #           message="""{}""".format(random.choice(RAIDHU)),
#            reply_to=event.message.id,
#        )

# @app.on_message(filters.command("pspam", PREFIX) & filters.me)
# async def pspam(bot, message): 
#   if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
#            return await e.reply(parse_mode=None, link_preview=None )
#        predator = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
 #       smex = await e.get_reply_message()
#        if len(predator) == 2:
#            message = str(predator[1])
#            print(message)
#            a = await e.client.get_entity(message)
#            g = a.id
 #           c = a.first_name
#            username = f"[{c}](tg://user?id={g})"
#            counter = int(predator[0])
#            for _ in range(counter):
#                reply = random.choice(RAID)
#                caption = f"{username} {reply}"
#                async with e.client.action(e.chat_id, "typing"):
 #                   await e.client.send_message(e.chat_id, caption)
#                    await asyncio.sleep(0.3)
#        elif e.reply_to_msg_id:             
#            a = await e.get_reply_message()
#            b = await e.client.get_entity(a.sender_id)
 #           g = b.id
#            c = b.first_name
 #           counter = int(predator[0])
#            username = f"[{c}](tg://user?id={g})"
 #           for _ in range(counter):
#                reply = random.choice(PORN)
#                caption = f"{username} {reply}"
 #               async with e.client.action(e.chat_id, "typing"):
#                    await e.client.send_message(e.chat_id, caption)
 #                   await asyncio.sleep(0.3)
    #    else:
 #           await e.reply( parse_mode=None, link_preview=None )
        
