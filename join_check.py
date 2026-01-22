async def is_joined(bot, user_id, channel_id):
    try:
        m = await bot.get_chat_member(channel_id, user_id)
        return m.status in ["member", "administrator", "creator"]
    except:
        return False