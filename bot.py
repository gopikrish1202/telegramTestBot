from telegram import Update
from telegram.ext import Application, CommandHandler
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Command handler function
async def start(update: Update, context):
    await update.message.reply_text('Hello, this is your bot!')

# Main function to run the bot
def main():
    """Start the bot."""
    application = Application.builder().token('7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI').build()

    # Command handler for "/start"
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Start polling
    application.run_polling()

if __name__ == '__main__':
    main()
