FROM python:3.11-slim-buster

ARG PACKAGE
ARG INDEX_URL

RUN apt-get update && apt-get install -y build-essential
RUN pip install -U pip \
  && pip install -U datadog ddtrace uwsgi

ADD requirements.txt .
ADD app.ini .

RUN pip install -r requirements.txt
RUN pip install $PACKAGE --index-url $INDEX_URL

CMD ["uwsgi", "app.ini"]
