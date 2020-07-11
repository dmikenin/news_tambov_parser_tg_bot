FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code/
RUN pip3 install -r /code/requirements.txt

WORKDIR /code

EXPOSE 3001
