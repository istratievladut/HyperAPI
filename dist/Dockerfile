FROM python:3.6.6-alpine

RUN apk add bash alpine-sdk libexecinfo-dev

ARG hyperapiversion="2"

RUN pip install http://pypi.hcube.cool/HyperAPI-Nitro/HyperAPI_Nitro-${hyperapiversion}-py3-none-any.whl

CMD ["python"]
