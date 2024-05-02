import telebot
import requests
import json

bot = telebot.TeleBot('6994914411:AAFGtlCtpzs8_Ch1QS3xGlV25NJzDcSPDe8')
API = '38d042c4d97bc86eef4a8bf746b8b365'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я Погодабот! Напиши название города и узнаешь температуру!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')
    else:
        bot.reply_to(message, f'Такого города не существует')

bot.polling(none_stop=True)