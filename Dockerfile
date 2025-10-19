# Poetry option

FROM python:3.12-slim

ARG POETRY_VERSION=1.8.3

WORKDIR /deployment-project

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    pip install --no-cache-dir poetry==${POETRY_VERSION}

COPY pyproject.toml poetry.lock /deployment-project/

ENV POETRY_VIRTUALENVS_CREATE=false

RUN poetry install --no-interaction --no-ansi --only main

COPY app/ /deployment-project/app

COPY model/ /deployment-project/model

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Requirements.txt option

# FROM python:3.12-slim

# WORKDIR /deployment-project

# COPY ./requirements.txt /deployment-project/requirements.txt

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends curl && \ 
#     pip install --no-cache-dir -r requirements.txt

# COPY /app /deployment-project/app

# COPY /model /deployment-project/model

# EXPOSE 8000

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]