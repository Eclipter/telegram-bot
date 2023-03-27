import aiogram

from settings import *

bot = telebot.TeleBot(TELEGRAM_BOT_API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, '<b>Доброго времени суток!</b>', parse_mode='HTML')
    sticker = open('sticker.webp')
    bot.send_sticker(message.chat.id, sticker)


bot.infinity_polling()
