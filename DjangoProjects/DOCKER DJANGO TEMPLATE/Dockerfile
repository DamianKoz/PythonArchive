# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

RUN pip install poetry

# install psycopg2 dependencies
RUN apt-get update \
  && apt-get install -y libpq-dev gcc python3-dev

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt \
  && pip install -r requirements.txt

COPY . /app
