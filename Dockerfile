FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir hatch && hatch env create

COPY app ./app
COPY app/main.py ./main.py