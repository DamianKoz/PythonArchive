# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry 

COPY poetry.lock pyproject.toml ./

RUN poetry export -f requirements.txt > requirements.txt

RUN pip install -r requirements.txt

COPY . .



