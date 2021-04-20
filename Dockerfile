FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /grandmetric

ADD . /grandmetric

COPY . /requirements.txt/grandmetric/requirements.txt

RUN pip install -r requirements.txt

COPY . /grandmetric