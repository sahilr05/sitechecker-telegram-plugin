from django import forms

from .models import TelegramAlertPlugin


class TelegramAlertForm(forms.ModelForm):
    class Meta:
        model = TelegramAlertPlugin
        widgets = {
            "telegram_id": forms.NumberInput(
                attrs={"class": "form-control", "type": "number", "min": 1}
            )
        }
        fields = ("telegram_id", "active_status")
