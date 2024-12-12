# import requests

# # Define the bot token and API URL
# BOT_TOKEN = "7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI"
# BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# # Define the parameters
# chat_id = "@gopitestbot12"
# text = "Custom bot message sent from Python script!"

# # Send the request
# response = requests.get(BASE_URL, params={"chat_id": chat_id, "text": text})

# # Check the response
# if response.status_code == 200:
#     print("Message sent successfully!")
# else:
#     print("Failed to send message:", response.text)
import requests
import time

# Define your bot token
BOT_TOKEN = "7981527875:AAEMoKR68iYkQzE2Ga9YYU3CZ08orBYy_xI"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Function to get updates (incoming messages)
def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"offset": offset, "timeout": 30}  # Long polling
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        print("Failed to get updates:", response.text)
        return []

# Function to send a message
def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"Message sent to {chat_id}: {text}")
    else:
        print("Failed to send message:", response.text)

# Main function to handle incoming messages
def main():
    last_update_id = None
    while True:
        updates = get_updates(offset=last_update_id)
        for update in updates:
            # Extract chat ID and message text
            chat_id = update["message"]["chat"]["id"]
            message_text = update["message"]["text"]

            # Process the message
            if message_text.lower() == "hello":
                send_message(chat_id, "Hi there! How can I help you?")
            elif message_text.lower() == "bye":
                send_message(chat_id, "Goodbye! Have a great day!")
            else:
                send_message(chat_id, "Sorry, I didn't understand that.")

            # Update the last update ID
            last_update_id = update["update_id"] + 1

        # Wait before polling again
        time.sleep(1)

if __name__ == "__main__":
    main()
