import random
import apiai
import telebot
import json
from telebot import types

bot = telebot.TeleBot(token='token')

addresses = {}

def casino():
    pass


def navigation(message):
    bot.send_message(message.chat.id, 'В каком районе вы живете?')
    if message.text == 'district1':
        district_ad = []
        for ad in addresses['district1']:
            district_ad.append(ad)
        bot.send_message(message.chat.id, 'Ближайшие магазины:')
        for ad in district_ad:
            bot.send_message(message.chat.id, '{ad}')



def order():
    pass


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Сделать заказ')
    item2 = types.KeyboardButton('Сыграть')
    item3 = types.KeyboardButton('Узнать адреса магазинов')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!\n Я - <b>{1.first_name}</b> помогу тебе сориентироваться в мире крафтовых напитков.'
                     .format(message.from_user,
                             bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.chat.type == 'private':
        if message.text == 'Сделать заказ':
            #order() здесь будет функция заказа
        elif message.text == 'Сыграть':
            #casino() здесь будет функция игры
            bot.send_message(message.chat.id, 'Good')
        elif message.text == 'Узнать адреса магазинов':
            navigation(message)
        else:
            bot.send_message(message.chat.id, 'please. replay')


bot.polling(none_stop=True)
