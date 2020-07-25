# SiteChecker Telegram bot

Telegram Bot plugin for Site Checker

## How to install 

Find python package in dist, download and install it.
```
pip install sc_telegram_bot.tar.gz
```

## Integrating in SiteChecker

* Add sc_telegram_plugin in settings > INSTALLED_APPS

```

INSTALLED_APPS = [
...
...
"sc_telegram_plugin",
]
```

* Add following url in sitechecker > accounts > urls.py

```
path("plugin/telegram_plugin",include("sc_telegram_plugin.urls", namespace="telegram_plugin")),
```
* Copy template from plugin to sitechecker > templates > plugins

* Run migrations