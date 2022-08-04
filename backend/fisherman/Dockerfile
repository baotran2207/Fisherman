FROM python:3.10.4-slim
COPY ./poetry.lock ./pyproject.toml ./
COPY ./app ./app
COPY ./.env ./.env
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev
ENV HOST="0.0.0.0"
ENV PORT=5000


ENTRYPOINT uvicorn app.main:app  --host ${HOST}  --port 5000
