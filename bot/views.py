from django.shortcuts import render

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
            active_status = form.cleaned_data.get("active_status")
            TelegramAlertPlugin.objects.filter(telegram_id=old_telegram_id).update( #NOQA
                telegram_id=new_telegram_id, active_status=active_status
            )
        except Exception:
            telegram_id = form.cleaned_data.get("telegram_id")
            active_status = form.cleaned_data.get("active_status")
            TelegramAlertPlugin.objects.create(
                telegram_id=telegram_id,
                alert_receiver=request.user,
                active_status=active_status,
            )

    context = {"form": form, "plugin_name": TelegramAlertPlugin.__name__}
    return render(request, "plugins/plugin.html", context)
