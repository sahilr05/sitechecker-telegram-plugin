import jsonpickle
import telegram
from django_telegrambot.apps import DjangoTelegramBot
from telegram.ext import CommandHandler
from checkerapp.models import AlertPlugin
# from .models import TelegramAlertPlugin
from django.db import models
from django.apps import apps
TelegramAlertPlugin = models.ForeignKey('bot.TelegramAlertPlugin', on_delete=models.CASCADE)

chat_ids = set()
bot_token = ***REMOVED***
# bot_token = ***REMOVED*** #temp bot
bot = telegram.Bot(token=bot_token)

def start(update, context):
    message = "Welcome ! I am Site Checker bot. Please enter your phone number using /register xxxxxxxxxx to proceed or /get_id to get your chat ID"
    update.message.reply_text(message)

def get_id(update, context):
    chat_id = update.message.chat_id
    message = f"Add {chat_id} in My Account > Alert Plugins > Telegram"
    update.message.reply_text(message)

def get_all_ids(update, context):
    chat_id = update.message.chat_id
    chat_ids.add(chat_id)
    update.message.reply_text(jsonpickle.encode(chat_ids))

def send_alert(message, user):
    bot.send_message(chat_id=user.telegram_id, text=message)

# def register(update, context):
#     try:
#         phone = context.args[0] # converting to tuple
#         check_phone = str(phone)
#         if check_phone in list(Profile.objects.values_list("phone", flat=True)):
#             user = Profile.objects.get(phone=phone).user
#             chat_id = update.message.chat_id
#             # TelegramAlertPlugin.objects.create(
#             #     telegram_id=chat_id, alert_receiver=user
#             # )
#             message = "Number Registered !"    
        
#         else:
#             message = "Number doesn't exist in check ! \nPlease ask admin to add your number for alerts"
#     except Exception as e:
#         print(e)
#         message = (
#             "Please send your number in the following syntax : /register xxxxxxxxxx"
#         )

#     update.message.reply_text(message)


def main():
    dp = DjangoTelegramBot.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get_id", get_id))
    dp.add_handler(CommandHandler("chat_ids", get_all_ids))
    # dp.add_handler(CommandHandler("register", register))
