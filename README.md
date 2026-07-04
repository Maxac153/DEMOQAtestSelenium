# DEMOQA test Selenium

## Описание

Цель проекта: получение навыков в написание автоматизированных авто тестов на Python.
Сайт для тестирования (<a href="https://demoqa.com">DEMOQA</a>).

## Окружение

Для того чтобы запустить тесты надо установить браузер chromium.

# Состав проекта

- Папка (tests) с Python тестами
- Папка (report) c отчётами

## Selenium тесты

Пример запуска Selenium тестов:

![tests_selenium.png](img/tests_selenium.png)

## Отчет по Selenium тестам

Пример отчета по Selenium тестам

![report_selenium.png](img/report_selenium.png)

Установка веб драйвера:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb
```

Запуск тестов

```bash
poetry run pytest -n 2 --dist=loadfile -m smoke
```

Отчёт

```bash
allure serve output/allure-results
```

##  TODO

~~1. Параллельный запуск тестов~~
~~2. Сбор Allure отчёта~~
~~3. Проверить разные браузеры~~
~~4. Разные разрешения у браузера параметр как у мобилки фул экран 2к 4к~~
5. Как сохранять логи har из браузера когда сломался тест
6. Понять как запускать разные версии браузеров (можно через докер вроде)
7. Понять как настроить "Система выполнения тестов" в allure