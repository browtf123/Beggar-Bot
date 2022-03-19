FROM python:3.10.3-slim-bullseye

RUN apt-get update; apt-get install -y curl

#RUN adduser --disabled-password worker
RUN adduser worker
USER worker
WORKDIR /home/worker
ENV PATH="/home/worker/.local/bin:/home/worker/.poetry/bin:${PATH}"

RUN pip install --upgrade pip
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN pip install poetry

COPY --chown=worker:worker poetry.lock .
COPY --chown=worker:worker pyproject.toml .
COPY --chown=worker:worker ./src/ ./src/

#RUN poetry install

ENTRYPOINT [ "/bin/bash" ]
