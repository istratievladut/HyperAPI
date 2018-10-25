FROM python:3.6.6-alpine

RUN apk add bash alpine-sdk libexecinfo-dev

ARG hyperapiversion="3"

RUN pip install http://pypi.hcube.cool/HyperAPI/HyperAPI-${hyperapiversion}-py3-none-any.whl

CMD ["python"]
