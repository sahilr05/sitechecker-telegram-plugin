# Generated by Django 3.0.6 on 2020-07-08 10:15
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("checkerapp", "0017_alertplugin_active_status")]

    operations = [
        migrations.CreateModel(
            name="TelegramAlertPlugin",
            fields=[
                (
                    "alertplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="checkerapp.AlertPlugin",
                    ),
                ),
                ("telegram_id", models.CharField(max_length=50)),
            ],
            options={"abstract": False, "base_manager_name": "objects"},
            bases=("checkerapp.alertplugin",),
        )
    ]
