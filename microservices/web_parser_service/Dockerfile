FROM python:3.10-slim-buster

WORKDIR /service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
RUN rm -rf tests

CMD ["faststream", "run", "main:app"]