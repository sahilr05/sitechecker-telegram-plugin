# SiteChecker Telegram bot

Telegram Bot plugin for Site Checker

## How to install

Find python package in dist, download and install it.
```
pip install sc_telegram_bot.tar.gz
```

## Integrating in SiteChecker

* Add bot in settings > INSTALLED_APPS

```
INSTALLED_APPS = [
...
...
"bot",
]
```

* Add following url in sitechecker > accounts > urls.py

```
path("plugin/telegram_plugin", include("bot.urls", namespace="telegram_plugin")),
```
* Run migrations
