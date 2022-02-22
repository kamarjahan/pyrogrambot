from pyrogram import Client, filters



Stuart=Client(
    "Pyrogram Bot",
    bot_token="bot token",
    api_id="api id",
    api_hash="api hash"
)

@Stuart.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("hi")

Stuart.run()
