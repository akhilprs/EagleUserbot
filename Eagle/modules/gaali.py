





async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")


@bot.on(admin_cmd(pattern="dreplyraid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="dreplyraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
