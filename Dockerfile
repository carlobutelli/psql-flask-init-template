FROM python:3.7
MAINTAINER Carlo Butelli <c.butelli@nxchange.com>

ADD . /code
WORKDIR /code

RUN pip3 install -r requirements/base.txt
RUN pip3 install gunicorn


CMD ["gunicorn", "--bind", "0.0.0.0:8080", "loki.wsgi:app"]