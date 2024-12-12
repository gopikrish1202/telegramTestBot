import asyncio
from telegram import Bot
from telegram.error import InvalidToken

token = '7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI'
chat_id = '@gopitestbot12'  # Ensure this is the correct chat ID or username

async def send_message():
    try:
        bot = Bot(token=token)
        await bot.send_message(chat_id=chat_id, text='Message sent from Postman')
        print("Message sent successfully!")
    except InvalidToken:
        print("Invalid token! Please check your token.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the async function
asyncio.run(send_message())
