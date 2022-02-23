from pyrogram import Client, filters



Stuart=Client(
    "Pyrogram Bot",
    bot_token="5153898163:AAE-DNHYOwy7xze2NZbDiSveDh8cUEgbnL4",
    api_id="9297449",
    api_hash="f8c528c480bcccd28df74a645275e446"
)

@Stuart.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("Hey bro sugamano?")

Stuart.run()
