# Лабораторная работа 8: Основы нагрузочного тестирования (k6)

## Установка k6 (macOS)
```bash
brew install k6
# Проверка
k6 version
```
Альтернатива (Docker):
```bash
# пример запуска скрипта через Docker
docker run -i loadimpact/k6 run - < scripts/get.js
```

## Объект тестирования
По умолчанию: `https://test.k6.io/` (можно заменить через `BASE_URL`).

Также добавлена локальная страница: `site/index.html`.

## Скрипты
- `scripts/get.js` — базовый скрипт с GET-запросом и `thresholds`.
- `scripts/scenarios.js` — сценарии с двумя нагрузками (10 VUs/30s и 50 VUs/10s).

Переменные окружения:
- `BASE_URL` — базовый URL (по умолчанию `https://test.k6.io`)
- `PATH` — путь (по умолчанию `/`)
- Для `get.js`: `VUS`, `DURATION`, `SLEEP`
- Для `scenarios.js`: `VUS1`, `DUR1`, `VUS2`, `DUR2`, `START2`

## Локальный стенд: запуск статической страницы
Из директории `lab8` поднимите простой сервер (Python 3):
```bash
cd /Users/nikitamarkin/labs/lab8
python3 -m http.server 8000
```
Страница будет доступна по `http://localhost:8000/site/`.

### Нагрузка k6 на локальную страницу
- Базовый тест (10 VUs, 30s):
```bash
BASE_URL=http://localhost:8000 PATH=/site/ k6 run scripts/get.js
```
- Два сценария (10 VUs/30s + 50 VUs/10s):
```bash
BASE_URL=http://localhost:8000 PATH=/site/ k6 run scripts/scenarios.js
```

## Анализ результатов
В стандартном выводе k6 обратите внимание на:
- Количество запросов: `http_reqs`
- Длительность: `http_req_duration` (p(90), p(95), p(99))
- Ошибки: `http_req_failed` (доля неуспешных запросов)
- RPS: `iterations/s`, суммарные метрики по сценариям
- Выполнение `thresholds`: PASS/FAIL

Примеры целевых метрик:
- 95-й перцентиль ответа < 800–1000ms
- Ошибки < 1%
- Пропускная способность (RPS) стабильна при росте нагрузки

## Полезно
- Генерируйте JSON-вывод для последующего анализа:
```bash
k6 run --summary-export=summary.json scripts/get.js
```
- Экспериментируйте с `ramping-vus`, `constant-arrival-rate` и др. экзекьюторами.
