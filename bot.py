# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    updater = Updater("446989268:AAHvmXYtah643DpQueAYYfbCK0-d4lgqPOs")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
	print('/start')

# Вызываем функцию - эта строчка собственно запускает бота
main()