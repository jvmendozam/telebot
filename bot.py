from telegram.ext import Updater, CommandHandler
#from config.auth import token

import logging
import requests
from bs4 import BeautifulSoup
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('AchicaynaBot')


def start(bot, update):
    logger.info('He recibido un comando start')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Soy un Achicayna, que entre los primeros pobladores de Canarias era el equivalente a un plebeyo."
    )

def gym(bot,update):
    arr = []
    r = requests.get("https://www.basic-fit.com/on/demandware.store/Sites-BFE-Site/es_ES/VirtuaGym-Events?club_id=f66c2398fcc64556a32115cd10af0db7&seotitle=Gimnasio%20Madrid%20Paseo%20de%20la%20Florida&seosequence=12/")
    soup = BeautifulSoup(r.content, 'html.parser')
    schedule_list = soup.find_all('ul', {'class': 'gxr-classes__list__inner js-gxr-list-inner'})
    for ultag in schedule_list:
        for litag in ultag.find_all('li'):
            schedule = litag.text.strip().replace('\n', ' ')
            schedule = ' '.join(schedule.split())
            arr.append(schedule)
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n'.join(arr)
    )

def my_ip(bot,update):
    params = (
    ('format', 'json'),)
    response = requests.get('https://api.ipify.org/', params=params)
    ip = str((json.loads(response.text))["ip"])
    bot.send_message(
        chat_id=update.message.chat_id,
        text="La ip es : " + ip 
    )


if __name__ == '__main__':

    updater = Updater(token="826201553:AAHtPO6KWEUNUzUefXHvOYCuDBCTs-HUfkU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('gym', gym))
    dispatcher.add_handler(CommandHandler('my_ip', my_ip))
    
    updater.start_polling()
    updater.idle()
