import requests
import random
import telebot
from bs4 import BeautifulSoup as bs

URL = 'https://www.anekdot.ru/last/good'
API_KEY = '6817452754:AAHeEXi-nKpknvtUC8qkvNNyWmqg0ByP02A'


def parser(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    return [c.text for c in jokes]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Hi, try write number from 1-9')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Try again')


bot.polling()
