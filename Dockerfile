FROM python:3.10-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

#RUN apt update

WORKDIR /app

from base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY poetry.lock pyproject.toml ./
RUN . /venv/bin/activate && poetry install --no-dev --no-root

#RUN poetry build && \
#    /venv/bin/pip install dist/*.whl

FROM base as final

COPY --from=builder /venv /venv
COPY docker-entrypoint.sh app.py ./
CMD ["./docker-entrypoint.sh"]
