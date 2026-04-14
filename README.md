# 📊 SPIMEX Trading Results Parser

Парсер для автоматического сбора и обработки бюллетеней по итогам торгов с сайта [СПбМТСБ (SPIMEX)](https://spimex.com/markets/oil_products/trades/results/).  

---

## Возможности

- Автоматический сбор ссылок на PDF-бюллетени с пагинацией (Selenium)
- Параллельное скачивание PDF-файлов (ThreadPoolExecutor)
- Извлечение таблиц из PDF с помощью `pdfplumber`
- Очистка и нормализация данных (удаление пробелов, приведение типов)
- Сохранение в базу данных через SQLAlchemy ORM
- Логирование процесса (консоль + файл)
- Поддержка Python 3.12+

---

## 🛠 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/D-Danis/working_with_database.git
```

### 2. Установить зависимости (через `uv`)

```bash
uv sync
```

### 3. Настроить переменные окружения

Создайте файл `.env` в корне проекта:

```env
DB_NAME=spimex_db
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=your_password
```

### 4. Запустить парсер

```bash
uv run python scr/project_2/main.py
```

---

## Конфигурация

| Переменная | Описание |
|------------|----------|
| `DB_NAME`  | Имя базы данных |
| `DB_HOST`  | Хост БД (localhost) |
| `DB_PORT`  | Порт (5432 для PostgreSQL) |
| `DB_USER`  | Пользователь БД |
| `DB_PASS`  | Пароль |

---

## Технологии

- Python 3.12
- `requests` / `selenium` / `pdfplumber`
- `pandas` / `numpy`
- `SQLAlchemy` + `psycopg2-binary`
- `uv` – менеджер пакетов
- `ruff` – линтинг и форматирование

---
