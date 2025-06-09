"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#PROXY = {
   # 'proxy_url': 'socks5://t1.learn.python.ru:1080',
    #'urllib3_proxy_kwargs': {
     #   'username': 'learn',
      #  'password': 'python'
   #}
#}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def otvet_planet(update, context):
    text_user = str(update.message.text)
    date=f'{datetime.date.today()}'
    planet = text_user
    result=''
    spisok={'/planet Venus':ephem.Venus,'/planet Jupiter':ephem.Jupiter,
            '/planet Mercury': ephem.Mercury, '/planet Mars':ephem.Mars, 
            '/planet Saturn': ephem.Saturn, '/planet Uranus':ephem.Uranus, 
            '/planet Neptune':ephem.Neptune, '/planet Pluto':ephem.Pluto,
            '/planet Sun':ephem.Sun}
    for key, value in spisok.items():
        if key==planet:
            result = ephem.constellation(value(date))
    update.message.reply_text(result)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", otvet_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
