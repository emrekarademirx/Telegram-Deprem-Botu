import requests
import telegram
import time

bot_token = 'BOT_TOKEN' # Telegram bot tokenınızı buraya girin
bot = telegram.Bot(token=bot_token)
chat_id = 'CHAT_ID' # Telegram sohbet ID'sini buraya girin

def get_earthquake_data():
    response = requests.get("http://www.koeri.boun.edu.tr/scripts/lst4.asp")
    data = response.text
    return data

while True:
    earthquake_data = get_earthquake_data()
    bot.send_message(chat_id=chat_id, text=earthquake_data)
    time.sleep(300) # Kodu her 5 dakikada bir çalıştırın
