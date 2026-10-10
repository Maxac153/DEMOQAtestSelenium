# DEMOQA test Selenium

## Описание

Сайт для тестирования (<a href="https://demoqa.com">DEMOQA</a>).

## Окружение

Для того чтобы запустить тесты надо установить браузер chromium и установить веб драйвер:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb
```

## Состав проекта

- Папка (tests) с Python тестами
- Папка (report) c отчётами

## Selenium и Api тесты

Запуск тестов

Описание параметров запуска:

```textmate

poetry run pytest -n <> --dist=loadfile -m smoke
```

Пример команды запуска:

```bash
poetry run pytest -n 2 --dist=loadfile -m smoke
```

### Allure отчет

Пример отчета по Selenium тестам

![report_selenium.png](img/report_selenium.png)

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
8. Разобраться с async
9. Понять как делать диаграмму с запусками тестов в allure
10. Дописать ui тесты book_store_application
11. Дописать ui тесты [.py](src/ui/demoq/selenium/tests/widgets/test_9_select_menu.py)
12. Написать тесты для playwright
13. Изучить флаки тесты в python
14. Как понять сколько потоков выделять