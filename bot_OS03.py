import telebot

BOT_TOKEN = '7438496820:AAG_qZPwIX5pmg89K7uhObhhClOKFMuKAQE'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я нахожусь на локальном сервере с автозапуском 😎")


if __name__ == "__main__":
    bot.polling(none_stop=True)