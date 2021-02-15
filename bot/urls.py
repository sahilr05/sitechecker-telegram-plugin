from django.urls import path

from . import views  # NOQA

app_name = "bot"

urlpatterns = [path("", views.telegram_plugin, name="telegram_pluginview")]
