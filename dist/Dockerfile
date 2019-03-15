FROM python:3.6.6-alpine

RUN apk add bash alpine-sdk libexecinfo-dev

ARG hyperapiversion="0"

RUN pip install -i https://pypi.hcube.cool/simple HyperAPI=="${hyperapiversion}"

CMD ["python"]
