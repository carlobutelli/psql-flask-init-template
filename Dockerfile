FROM python:3.9.16-alpine3.16
MAINTAINER Carlo Butelli <dev.butelli@gmail.com>

ENV INSTALL_PATH /code
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements /code/requirements
RUN apk add py-configobj libusb py-pip python3-dev gcc linux-headers
RUN apk add --no-cache --virtual .build-deps zlib-dev jpeg-dev \
  build-base postgresql-dev libffi-dev \
    && pip3 install -r requirements/prod.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

RUN apk add --no-cache file-dev
COPY . /code

RUN chmod 755 docker_entrypoint.sh
ENTRYPOINT ["sh", "docker_entrypoint.sh"]
CMD ["uwsgi", "--need-app", "--logformat", "[%(ltime)] [UWSGI] \"%(method) %(uri) %(proto)\" %(status) %(size) \"%(referer)\" \"%(uagent)\""]
