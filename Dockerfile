FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/
