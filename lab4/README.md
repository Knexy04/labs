# Лабораторная работа 4: Позитивные и негативные UI-сценарии (Page Object)

## Окружение
- Python 3.10+
- Chrome (и chromedriver через webdriver-manager)

Установка зависимостей:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Объект тестирования
Локальная страница формы обратной связи: `site/contact.html`.
Тесты работают офлайн, Selenium открывает локальный `file://` URL.

## Структура
- `site/contact.html` — форма с базальной валидцией и сообщениями об ошибках/успехе
- `pages/base_page.py` — базовый класс Page Object
- `pages/contact_page.py` — объект страницы формы
- `tests/test_contact_form.py` — позитивный и негативный сценарии
- `pytest.ini` — конфигурация pytest

## Запуск тестов
```bash
pytest -v
```
Headless-режим:
```bash
HEADLESS=1 pytest -v
```

## Сценарии
- Позитивный: заполнение валидными данными, отправка, проверка сообщения об успехе
- Негативный: отправка с пустым обязательным полем (Name), проверка текста ошибки

## Примечания
- Локаторы стабильные: `id` у инпутов и сообщений (`name`, `email`, `message`, `error-*`, `success-message`).
- При необходимости вы можете заменить локальную страницу на реальную, указав URL в методе `open`.
