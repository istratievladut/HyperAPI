FROM python:3.6.6-alpine

RUN apk add bash alpine-sdk libexecinfo-dev

ARG hyperapiversion="0"

RUN pip install s3://pypi.hcube.cool/HyperAPI-Nitro/HyperAPI_Nitro-${hyperapiversion}-py3-none-any.whl

CMD ["python"]
