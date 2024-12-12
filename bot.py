import asyncio
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters
from telegram.error import InvalidToken
import logging

token = '7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI'
chat_id = '@gopitestbot12'  # Ensure this is the correct chat ID or username

# Set up logging to get more information if needed
logging.basicConfig(level=logging.INFO)

# Async function to send a message
async def send_message(bot, chat_id, text):
    try:
        await bot.send_message(chat_id=chat_id, text=text)
        print("Message sent successfully!")
    except InvalidToken:
        print("Invalid token! Please check your token.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to handle incoming messages and respond to the user
def handle_message(update, context):
    user_message = update.message.text
    bot = context.bot
    chat_id = update.message.chat_id
    print(f"Received message: {user_message} from chat ID: {chat_id}")

    # Respond to the user based on their message
    response = f"You said: {user_message}"
    
    # Send a reply using the async send_message function
    asyncio.run(send_message(bot, chat_id, response))

def main():
    # Create an Updater object to receive and handle updates
    updater = Updater(token=token, use_context=True)

    # Get the dispatcher to register the handler
    dispatcher = updater.dispatcher

    # Register a message handler that listens for text messages
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
    dispatcher.add_handler(message_handler)

    # Start the bot
    print("Bot is now running. It will reply to any incoming messages...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
