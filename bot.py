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


