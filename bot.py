import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token and webhook URL
TOKEN = os.getenv("7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI")
WEBHOOK_URL = os.getenv("https://telegramtestbot-ruqb.onrender.com")

# Define a basic command handler (for example, `/start`)
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello, I am your bot!')

# Create the application and add handlers
async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Add a command handler (example `/start`)
    application.add_handler(CommandHandler("start", start))

    # Set up the webhook
    await application.bot.set_webhook(WEBHOOK_URL)

    # Disable polling by not calling run_polling. Webhook is now handling the updates.
    # The bot will now listen for updates only through the webhook.
    # No polling method is invoked here, so it's fully webhook-based.

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
