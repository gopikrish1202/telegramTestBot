import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Get your bot token and webhook URL from environment variables
TOKEN = os.getenv("7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI")  # Now fetches the BOT_TOKEN from the environment
WEBHOOK_URL = os.getenv("https://telegramtestbot-ruqb.onrender.com")  # Fetches the WEBHOOK_URL from the environment

# Define a basic command handler (for example, `/start`)
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello, I am your bot!')

# Create the application and add handlers
async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Add a command handler (example `/start`)
    application.add_handler(CommandHandler("start", start))

    # Set up the webhook
    if not WEBHOOK_URL:
        logger.error("Webhook URL is missing. Make sure to set the WEBHOOK_URL environment variable.")
        return

    try:
        await application.bot.set_webhook(WEBHOOK_URL)
        logger.info(f"Webhook set to {WEBHOOK_URL}")
    except Exception as e:
        logger.error(f"Failed to set webhook: {e}")
        return

    # Disable polling by not calling run_polling. Webhook is now handling the updates.
    # The bot will now listen for updates only through the webhook.
    logger.info("Bot is now listening for updates through the webhook.")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
