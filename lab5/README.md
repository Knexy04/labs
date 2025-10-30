# Лабораторная работа 5: Тестирование REST API (Postman + Python)

## Объект тестирования
Публичное API: `https://jsonplaceholder.typicode.com/`
Базовый URL для Python-тестов: `https://jsonplaceholder.typicode.com`.

## Часть 1 — Ручное тестирование в Postman
1) Создайте коллекцию `JSONPlaceholder Demo` и добавьте запросы:
- GET Post: `GET https://jsonplaceholder.typicode.com/posts/1`
- POST Create Post: `POST https://jsonplaceholder.typicode.com/posts` (Body: JSON `{ "title": "foo", "body": "bar", "userId": 1 }`)
- PUT Update Post: `PUT https://jsonplaceholder.typicode.com/posts/1` (Body: JSON `{ "id": 1, "title": "updated", "body": "lorem", "userId": 1 }`)

2) Для каждого запроса добавьте Tests (JavaScript):
- GET Post
```javascript
pm.test("Status is 200", function () { pm.response.to.have.status(200); });
const json = pm.response.json();
pm.test("Has expected fields", function () {
  pm.expect(json).to.have.property("id", 1);
  pm.expect(json).to.have.property("userId");
  pm.expect(json).to.have.property("title");
  pm.expect(json).to.have.property("body");
});
```

- POST Create Post
```javascript
pm.test("Status is 201", function () { pm.response.to.have.status(201); });
const json = pm.response.json();
pm.test("Echoed fields and id present", function () {
  pm.expect(json.title).to.eql("foo");
  pm.expect(json.body).to.eql("bar");
  pm.expect(json.userId).to.eql(1);
  pm.expect(json).to.have.property("id");
});
```

- PUT Update Post
```javascript
pm.test("Status is 200", function () { pm.response.to.have.status(200); });
const json = pm.response.json();
pm.test("Fields updated", function () {
  pm.expect(json.id).to.eql(1);
  pm.expect(json.title).to.eql("updated");
  pm.expect(json.body).to.eql("lorem");
  pm.expect(json.userId).to.eql(1);
});
```

3) Запустите Collection Run, зафиксируйте результаты (скрин/заметки).

## Часть 2 — Автотесты на Python (requests + pytest)
Установка зависимостей:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Запуск тестов:
```bash
pytest -v
```

Переменные окружения:
- `API_BASE_URL` — базовый URL API (по умолчанию `https://jsonplaceholder.typicode.com`)

Сценарии реализованы в `tests/test_reqres_api.py` (переиспользован файл):
- GET `/posts/1` — проверка 200 и структуры
- POST `/posts` — проверка 201 и полей ответа
- PUT `/posts/1` — проверка 200 и обновленных полей
- Негативный GET `/posts/999999` — 200 и пустой объект `{}` (особенность JSONPlaceholder)
