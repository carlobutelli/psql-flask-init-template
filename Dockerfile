FROM python:3.7
MAINTAINER Carlo Butelli <c.butelli@nxchange.com>

ADD . /code
WORKDIR /code

RUN pip install -r requirements/base.txt
RUN pip install gunicorn


CMD ["gunicorn", "--bind", "0.0.0.0:8080", "loki.wsgi:app"]