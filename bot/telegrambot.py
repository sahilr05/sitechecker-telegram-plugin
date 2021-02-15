import logging
import os

import telegram

logger = logging.getLogger(__name__)
bot = telegram.Bot(token=os.getenv("TG_BOT_TOKEN", "**or add token here**"))


def send_alert(message, user):
    bot.send_message(chat_id=user.telegram_id, text=message)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
