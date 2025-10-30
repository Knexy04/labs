# Лабораторная работа 7: Тестирование мобильного приложения (Appium)

## Ручное тестирование
См. чек-лист `checklist.md` — он покрывает жесты, ориентации, прерывания, сеть, память и др.

## Автоматическое тестирование (Android, Appium)
### Предварительные требования
- Node.js + Appium Server
```bash
npm install -g appium
appium -v
appium driver install uiautomator2
```
- Java JDK + Android SDK + platform-tools в PATH
- Эмулятор Android (AVD) или реальное устройство с включенным USB debugging

### Создание/запуск эмулятора (пример)
```bash
# Запустить AVD из Android Studio (AVD Manager)
# или через CLI (если настроено):
avdmanager list avd
emulator -avd <YOUR_AVD_NAME>
```

### Запуск Appium Server
```bash
appium
# по умолчанию: http://127.0.0.1:4723
```

### Установка зависимостей Python и запуск тестов
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Запуск pytest (ANDROID КАЛЬКУЛЯТОР)
pytest -v
```

Переменные окружения (опционально):
- `APPIUM_URL` (по умолчанию `http://127.0.0.1:4723`)
- `DEVICE_NAME` (по умолчанию `Android Emulator`)
- `PLATFORM_VERSION` (например `14`)
- `APP_PACKAGE` (по умолчанию `com.android.calculator2`)
- `APP_ACTIVITY` (по умолчанию `.Calculator`)

### Что делает тест
- Открывает приложение Калькулятор и проверяет, что текущее `current_package` совпадает с `APP_PACKAGE`.
- Пытается (best-effort) нажать `2 + 3 =` при наличии стандартных селекторов. Из-за различий OEM тест не падает, если элементы не найдены.

## Структура
- `checklist.md` — чек-лист ручного тестирования
- `conftest.py` — фикстура `android_driver` (Appium)
- `tests/test_android_calculator.py` — пример автотеста
- `requirements.txt` — зависимости (Appium client, pytest)
