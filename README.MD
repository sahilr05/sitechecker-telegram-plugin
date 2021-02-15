# SiteChecker Telegram bot

Telegram Bot plugin for Site Checker

## How to install

* Add bot token in ```telegrambot.py```
* Run following command
```
python manage.py sdist
```

* Navigate to ```dist``` and run following command to install package
```
pip install <package name>
```

## Integrating with SiteChecker

1. Add bot in settings > INSTALLED_APPS
```
INSTALLED_APPS = [
...
...
"bot",
]
```

2. Add following url in sitechecker > accounts > urls.py
```
path("plugin/telegram_plugin", include("bot.urls", namespace="telegram_plugin")),
```

3. Run migrations

Go to [https://telegram.me/userinfobot](@userinfobot) and get your ```chat id```
Enter ```chat id``` obtained from @userinfobot in
```
My account > Alert Plugins > Telegram Plugin
```
## Credits

Required packages:
[Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)
