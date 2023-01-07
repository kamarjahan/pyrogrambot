import os
import requests
from PIL import Image
from io import BytesIO

from telegram.ext import Updater, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm an autofilter bot. Send me a picture and I'll apply a filter to it.")

def filter_picture(update, context):
    # Check if the message is a photo
    if update.message.photo:
        # Get the largest photo from the list of photos
        photo = update.message.photo[-1]
        file_id = photo.file_id
        file = context.bot.get_file(file_id)
        file_url = file.file_path
        # Download the photo
        response = requests.get(f"https://api.telegram.org/file/bot{TOKEN}/{file_url}")
        image = Image.open(BytesIO(response.content))
        # Apply a filter to the photo
        image = image.filter(ImageFilter.BLUR)
        # Save the filtered photo to a file
        image.save("filtered_photo.jpg")
        # Send the filtered photo back to the user
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("filtered_photo.jpg", "rb"))

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(5849769037:AAFsz6rZz11ia8RxE9Lc1rEHm3EBYlV4OME, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, filter_picture))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == "__main__":
    main()
