#!

import logging
from telegram import ReplyKeyboardMarkup, Update, Bot, ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    PicklePersistence,
    CallbackContext,
)
import sys
import http.client
import calendar
import time
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


import os
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = os.environ['BOT_TOKEN']
robot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)

debug = os.environ['DEBUG']


if debug == "True":
    chat_id = os.environ['DEBUG_ID']
    interval = 1

if debug == "False":
    chat_id = os.environ['GROUP_ID']
    interval = 2

def SendMessage(message):
    robot.send_message(chat_id=chat_id, text=str(message))
    return


if __name__ == '__main__':
    args = sys.argv
    globals()[args[1]](*args[2:])


#CRON STUFF

# 0 6 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Good Morning. I request you take me out if I haven't been out yet. I've been trying to hold all night."
# 0 7 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Now that I've had my breakfast, please take me out again. 💩"
# 0 10 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "I've been sleeping again till now. Let me go out again for a wee."
# 0 12 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Maybe a good idea to go stretch my legs outside, some fresh air and a bit of sun."
# 0 14 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Take me outside quickly before Mom come's home!"
# 0 16 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "If there's no monkeys waiting to kill me outside, please may I go outside?"
# 0 18 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "Okay, I need to go empty my tummy before dinner. Oh yes!"
# 0 20 * * * /home/ronald/cron/dogpoop/doggybot/venv/bin/python3 /home/ronald/cron/dogpoop/doggybot/bot.py SendMessage "I'm ready to go sleep. Let me out for 15 minutes and then feed me a sausage! Good Night."
