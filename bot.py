import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import signal
import sys

# Enable logging to track any issues
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your start command
def start(update, context):
    update.message.reply_text("Hello! I'm your bot.")

# Define your main function
def main():
    # Replace with your bot's token
    token = '7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI'

    # Create Updater object and pass your bot's token
    updater = Updater(token, use_context=True)

    # Add handlers (e.g., command handler)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Start polling for updates
    updater.start_polling()
    logger.info("Bot is polling...")

    # Block until you receive a signal to stop
    updater.idle()

# Function to handle graceful shutdown
def shutdown(signum, frame):
    logger.info("Shutting down gracefully...")
    sys.exit(0)

# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

if __name__ == '__main__':
    main()
