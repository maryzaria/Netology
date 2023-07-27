import os
from datetime import date
from dotenv import load_dotenv

from application.salary import calculate_salary
from application.db.people import get_employees

from telebot import TeleBot

load_dotenv()
token = os.getenv('TOKEN')
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.chat.first_name if message.chat.first_name else ''
    text = f'Hi, {name}' if name else 'Hi, '
    bot.reply_to(message, text + 'I am EchoBot!')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
    print(date.today().strftime('%d.%m.%Y'))
    calculate_salary()
    get_employees()
