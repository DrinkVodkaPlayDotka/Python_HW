# Используем базовый образ Python 3.11
FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей (poetry.lock и pyproject.toml) внутрь контейнера
COPY poetry.lock pyproject.toml /app/

# Устанавливаем инструмент для управления зависимостями poetry
RUN pip install poetry

# Устанавливаем зависимости, указанные в файле pyproject.toml
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Копируем все файлы из текущей директории (кроме Dockerfile) внутрь контейнера
COPY . /app

# Запускаем веб-сервер uvicorn с указанными параметрами
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
