# import asyncio
# from telegram import Bot
# from telegram.ext import Application, MessageHandler, filters
# from telegram.error import InvalidToken
# import logging

# token = '7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI'
# chat_id = '@gopitestbot12'  # Ensure this is the correct chat ID or username

# # Set up logging to get more information if needed
# logging.basicConfig(level=logging.INFO)

# # Async function to send a message
# async def send_message(bot, chat_id, text):
#     try:
#         await bot.send_message(chat_id=chat_id, text=text)
#         print("Message sent successfully!")
#     except InvalidToken:
#         print("Invalid token! Please check your token.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Function to handle incoming messages and respond to the user
# async def handle_message(update, context):
#     user_message = update.message.text
#     bot = context.bot
#     chat_id = update.message.chat_id
#     print(f"Received message: {user_message} from chat ID: {chat_id}")

#     # Respond to the user based on their message
#     response = f"You said: {user_message}"
    
#     # Send a reply using the async send_message function
#     await send_message(bot, chat_id, response)

# def main():
#     # Create an Application object to receive and handle updates
#     application = Application.builder().token(token).build()

#     # Register a message handler that listens for text messages
#     message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
#     application.add_handler(message_handler)

#     # Start the bot
#     print("Bot is now running. It will reply to any incoming messages...")
#     application.run_polling()

# if __name__ == "__main__":
#     main()

import asyncio
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import logging

# Telegram bot token
TOKEN = '7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI'

# Google Search API key and Custom Search Engine ID
GOOGLE_API_KEY = 'AIzaSyB2HZOyAOID5pKxWy-PAjK4O8OWv8rAHnA'  # Your API key
GOOGLE_CX = '8031511dbf0284216'  # Your Search Engine ID
GOOGLE_SEARCH_URL = 'https://www.googleapis.com/customsearch/v1'

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to query Google Custom Search API
def search_google(query):
    params = {
        'q': query,
        'key': GOOGLE_API_KEY,
        'cx': GOOGLE_CX,
        'num': 3  # Number of results to fetch
    }
    response = requests.get(GOOGLE_SEARCH_URL, params=params)
    if response.status_code == 200:
        results = response.json().get('items', [])
        return [f"{result['title']}: {result['link']}" for result in results]
    else:
        return [f"Error {response.status_code}: {response.reason}"]

# Async function to handle /search command
async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text("Please provide a query after /search.")
        return

    results = search_google(query)
    reply = "\n\n".join(results) if results else "No results found."
    await update.message.reply_text(reply)

# Async function to handle general messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

def main():
    # Create Application object
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("search", search_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot is now running. Use /search <query> to search the web.")
    application.run_polling()

if __name__ == "__main__":
    main()
