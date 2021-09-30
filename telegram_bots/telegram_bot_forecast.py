from config import TOKEN
import telebot
from weather_forecast_example import *

my_city = CityInfo()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Hello {message.from_user.first_name}!</b>\nChoose your city"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(commands=['city'])
def city(message):
    send_mess = f"<b>Choose a city for request.</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(commands=['units'])
def measure_units(message):
    send_mess = f"<b>Choose a units measurement mode.</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def respond(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "metric" or get_message_bot == "imperial":
        my_city.units = get_message_bot
    else:
        my_city.name = get_message_bot
    bot.send_message(message.chat.id, my_city.get_forecast(), parse_mode='html')


@bot.message_handler(commands=['forecast'])
def measure_units(message):
    send_mess = f"<b>Choose a units measurement mode.</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)
