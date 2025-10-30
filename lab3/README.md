# Лабораторная работа 3: Первые UI-автотесты (Python + Selenium)

## Окружение
- Python 3.10+
- pip

Установка зависимостей:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Быстрый старт
- Открыть/закрыть браузер:
```bash
python open_close_browser.py
```

- Запустить автотесты:
```bash
pytest -v
```

Переменные окружения (необязательно):
- `BROWSER` = `chrome` | `firefox` (по умолчанию: chrome)
- `HEADLESS` = `1` включает headless-режим (по умолчанию: выключен)

Примеры:
```bash
BROWSER=firefox pytest -v
HEADLESS=1 pytest -v
```

## Объект тестирования
Используется публичный демо-сайт SauceDemo: `https://www.saucedemo.com/`
- username: `standard_user`
- password: `secret_sauce`

## Структура
- `open_close_browser.py` — простой скрипт инициализации WebDriver.
- `conftest.py` — фикстура `driver` для pytest, настройка браузера.
- `tests/test_login.py` — тест успешного логина.
- `manual-selectors.md` — заметки по ручному анализу стабильности селекторов.

## Примечания
- Драйверы браузеров автоматически управляются через `webdriver-manager`.
- Тест использует явные ожидания (`WebDriverWait`) для стабильности.
