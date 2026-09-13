# Генератор паролей (Python)

[![hexlet-check](https://github.com/khanbro406-debug/python-basics-free-project-391/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/khanbro406-debug/python-basics-free-project-391/actions/workflows/hexlet-check.yml)

Небольшое приложение на Python — генератор паролей с проверкой надёжности.

Программа генерирует пароли из выбранных наборов символов и оценивает надёжность любого пароля.

Проект закрепляет основы программирования: строки, числа, условия, циклы и функции с параметрами.

## Стек

- Python 3
- Git
- GitHub
- GitHub Actions

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/khanbro406-debug/python-basics-free-project-391.git
cd python-basics-free-project-391
```

## Использование

Запустите программу:

```bash
python main.py
```

Программа покажет примеры генерации паролей и проверки их надёжности.

### Пример запуска

```text
== Генерация паролей ==
буквы и цифры:    5vjehYzZEzZ0
со спецсимволами: ...

== Проверка надёжности ==
abc        -> Слабый пароль (оценка 1 из 5)
abcdef1234 -> Средний пароль (оценка 3 из 5)
Abcdef123! -> Очень надежный пароль (оценка 5 из 5)
```

## О Хекслете

Учебный проект выполнен в рамках курса Хекслета по основам Python.

[Хекслет](https://ru.hexlet.io/programs/python-basics-free)
