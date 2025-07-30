# Парсер топ аниме с YummyAni

Скрипт на Python, который собирает **топ-50 аниме** с сайта [YummyAni](https://site.yummyani.me/catalog/top) и выводит основную информацию: **название**, **рейтинг** и **ссылку** на страницу.

## Возможности

- Парсит список самых популярных аниме
- Извлекает:
  - Название аниме
  - Рейтинг
  - Ссылку на страницу
- Выводит данные в удобном читаемом виде

## Используемые библиотеки

- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)
- [`lxml`](https://pypi.org/project/lxml/)

## Установка и запуск

1. Установите зависимости:
   ```bash
   pip install requests beautifulsoup4 lxml
