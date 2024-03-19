FROM python:latest

WORKDIR /FpvAppContainer
COPY  requirements.txt ./


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY FpvApp ./

