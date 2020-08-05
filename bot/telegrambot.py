import jsonpickle
from checkerapp.models import AlertPlugin
from django.db import models
from django.apps import apps

from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot

import logging
logger = logging.getLogger(__name__)

def start(bot, update):
    message = "Welcome ! I am Site Checker bot. Please enter /get_id to get your chat ID to register in Site Checker"
    bot.sendMessage(update.message.chat_id, text=message)

def send_alert(message, user):
    bot.send_message(chat_id=user.telegram_id, text=message)
    
def get_id(bot, update):
    chat_id = update.message.chat_id
    message = f"Add {chat_id} in My Account > Alert Plugins > Telegram"
    bot.sendMessage(update.message.chat_id, text=message)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Loading handlers for telegram bot")

    dp = DjangoTelegramBot.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get_id", get_id))

    # log all errors
    dp.add_error_handler(error)


