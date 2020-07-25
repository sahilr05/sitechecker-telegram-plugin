from django.conf.urls import url

from . import views

from django.contrib import admin
from django.urls import path
from bot import views

app_name = "bot"

urlpatterns = [
    path("", views.telegram_plugin, name="telegram_pluginview"),
]
