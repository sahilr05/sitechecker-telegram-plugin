from checkerapp.models import AlertPlugin, BaseCheck, AlertSent
from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User
from celery import shared_task
from django.db.models import Q
from .telegrambot import send_alert
# from sc_telegram_plugin import bot

class TelegramAlertPlugin(AlertPlugin):
        
    '''
    0 -> Normal
    1 -> Warning
    2 -> Critical

    Refer following thread -> www.github.com/xxxxxxx
    '''
    
    severe_level = 2 #should be same as severity level of check or else it won't work
    url = 'accounts:telegram_plugin:telegram_pluginview'
    telegram_id = models.CharField(max_length=50)

    @shared_task
    def send_alert_task(task_obj):
        return 'Telegram Plugin'
        # check_obj = task_obj["base_check_obj"]
        # message = str(check_obj.content_object) + " is down"
        # users = list(check_obj.service_set.first().users.all())
        # for user in users:
            
        #     telegram_user_obj = TelegramAlertPlugin.objects.filter(Q (alert_receiver=user) and Q(active_status=True)).first()
        #     send_alert(message, telegram_user_obj)
        #     AlertSent.objects.create(check_obj=check_obj)
        #     return "Success !"
