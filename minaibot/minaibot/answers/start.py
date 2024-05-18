from telebot import types
from minaibot.answers import cache


def start(bot, message, server):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/stop")
    markup.add(btn1, btn2)
    if message.chat.id in cache and cache[message.chat.id] == message.text:
        bot.send_message(message.chat.id,
                         text=f"Мы уже здаровались..",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         text=f"Привет, я бот, созданный через фреймворк minaibot!",
                         reply_markup=markup)
    cache[message.chat.id] = message.text


def stop(bot, message, server):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/stop")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text=f"Меня не остановить!",
                     reply_markup=markup)
