import os
import logging
import requests
from flask import Flask, request
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# Initialize the Flask app
app = Flask(__name__)

# Telegram bot token (use securely via environment variable or .env file)
TOKEN = '7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI'  # Replace with your bot token
bot = Bot(token=TOKEN)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to handle /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your Telegram bot.")

# Function to handle text messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Set up the dispatcher
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# Add handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Route to handle webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse incoming message
    json_str = request.get_data().decode('UTF-8')
    update = telegram.Update.de_json(json_str, bot)
    
    # Dispatch the update to the bot handler
    dispatcher.process_update(update)
    return 'OK'

# Set webhook with Telegram API (this should be done once during deployment)
def set_webhook():
    url = f"https://your-app-name.onrender.com/webhook"  # Replace with your Render app URL
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={url}")
    print(response.text)

# Main entry point to run the Flask app
if __name__ == '__main__':
    set_webhook()  # Optional, run this once to set webhook
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
