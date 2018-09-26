FROM python:3.6.6-alpine

WORKDIR /opt

RUN apk add bash alpine-sdk libexecinfo-dev

ARG hyperapi_version=""

RUN mkdir HyperAPI && wget https://s3.eu-west-1.amazonaws.com/hc-jenkins-ci/HyperAPI/HyperAPI-${hyperapi_version}.tar.gz && tar -xzvf HyperAPI-${hyperapi_version}.tar.gz -C HyperAPI

WORKDIR /opt/HyperAPI

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV PYTHONPATH=..

CMD ["python"]
