from django.shortcuts import render
from django_telegrambot.apps import DjangoTelegramBot  # NOQA

from .forms import TelegramAlertForm
from .models import TelegramAlertPlugin


def telegram_plugin(request):
    user = request.user
    try:
        telegram_obj = TelegramAlertPlugin.objects.filter(
            alert_receiver=user.pk
        ).first()
    except Exception:
        telegram_obj = None

    form = TelegramAlertForm(request.POST or None, instance=telegram_obj)

    if request.method == "POST" and form.is_valid():
        try:
            old_telegram_id = (
                TelegramAlertPlugin.objects.filter(alert_receiver=user.pk)
                .first()
                .telegram_id
            )
            new_telegram_id = form.cleaned_data.get("telegram_id")
            TelegramAlertPlugin.objects.filter(
                telegram_id=old_telegram_id
            ).update(  # NOQA
                telegram_id=new_telegram_id
            )
        except Exception:
            telegram_id = form.cleaned_data.get("telegram_id")
            TelegramAlertPlugin.objects.create(
                telegram_id=telegram_id, alert_receiver=request.user
            )

    context = {"form": form, "plugin_name": TelegramAlertPlugin.__name__}
    return render(request, "plugins/plugin.html", context)
