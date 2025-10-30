# Лабораторная работа 6: Модульные тесты (Unit Tests)

Цель: написать модульные тесты для изолированных функций/методов с использованием `pytest`, применяя параметризацию и проверку исключений.

## Объект тестирования
Класс `Calculator` (`calculator.py`) с методами:
- `add(*numbers) -> float`
- `divide(numerator, denominator) -> float` (должен бросать `ZeroDivisionError` при делении на ноль)
- `is_prime_number(value: int) -> bool`

## Установка зависимостей
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск тестов
```bash
pytest -v
```

## Что покрыто тестами
- Параметризованные кейсы для `add` (несколько наборов чисел, включая пустой)
- Параметризованные кейсы для `divide` (валидные деления)
- Проверка исключения для `divide` при делении на ноль
- Параметризованные кейсы для `is_prime_number` (типичные значения, граничные случаи)

Файлы:
- `calculator.py` — реализация класса
- `tests/test_calculator.py` — модульные тесты (pytest + параметризация)
