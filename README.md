# Deployment Project – FastAPI + Docker + TensorFlow inference

A simple example that wraps a TensorFlow/Keras model behind a FastAPI HTTP API.  
The example is containerised with Docker, uses **Poetry** for dependency management, and ships with a health‑check and simple structured logging.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Quick start (Docker Compose)](#quick-start-docker-compose)
4. [Running locally](#running-locally)
5. [API reference](#api-reference)

## Overview
- **FastAPI** provides the HTTP layer (`/predict`, `/health`).
- **TensorFlow 2.x** loads a pre‑trained Keras model (`MODEL_PATH`).
- **Pydantic** (`PredictionsResponse`) validates the JSON response.
- **Poetry** handles the dependencies.
- **Docker‑Compose** builds and runs the project, exposing it on port **8000**.

## Prerequisites

Docker or Docker alternatives, Poetry and Python (3.12) are required to run the project.
Furthermore, the project requires a CNN model (h5 or keras format) accepting an image to be placed in a folder in the root directory, e.g., `model/the_cnn_model.h5`.
The .env file has to be specified in the root directory with the following variables.

| Variable | Description |
|----------|-------------|
| `MODEL_PATH` | Relative path to the model file, e.g. `/model/the_cnn_model.h5` |
| `POETRY_VERSION` | Poetry version used in the Dockerfile (default `1.8.3`). |

## Quick start (Docker Compose)

Clone the repo, perform the [prerequisites](#prerequisites) including the placement of a CNN model and creation of .env file.

Docker could be started with the following command in the root directory.

```bash
# or just docker compose up --build to keep logs visible
docker compose up --build -d
```

Docker could be verified using the following command.

```bash
docker compose ps
```

Docker logs could be checked using the following command.

```bash
docker compose logs deployment-project
```

The API should be reachable using `http://localhost:8000/docs`.

Remeber to stop and clean Docker when it is not required.

## Running locally

Clone the repo, perform the [prerequisites](#prerequisites) including the placement of a CNN model and creation of .env file.

> Useful for rapid iteration or debugging the model code.

Install the project dependencies, for example, using the following command in the root directory.

```bash
poetry install
```

Start locally using the following command.

```bash
poetry run start
```

## API reference

| Method | Path | Description | Request | Response |
|--------|------|-------------|---------|----------|
| **POST** | `/predict` | Run inference on an uploaded image (JPEG/PNG). | `multipart/form-data` with a single field **file** (the image). | `200 OK` → `{"probabilities": [float, ...]}` |
| **GET** | `/health` | Simple health check for Docker. | – | `200 OK` → `{"status":"healthy"}` |