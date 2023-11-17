# FastAPI app


* FastAPI app
* MongoDB integration
* Dockerfile and docker-compose integations

---

## Dependencies

* Python 3.10.12
* Poetry 1.5.1
* Docker-compose 2.6.0

---


## Usage

After successful build & run, you can open http://localhost:8000/docs

---

## Installation

Before doing something, make sure that you have

1. copied .env.example to .env
2. modified values in .env according to your realm

---

> docker-compose up --build


## Tests

>  poetry install --only test

>  poetry run pytest