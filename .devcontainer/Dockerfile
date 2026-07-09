FROM python:slim

WORKDIR /src

COPY . .
RUN apt update && apt -y install gcc git
RUN pip install -r dev-requirements.txt
