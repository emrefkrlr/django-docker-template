# En güncel stabil Python Alpine sürümü
FROM python:3.12-alpine

LABEL maintainer="emrefikirlier@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

# venv oluşturma ve pip güncelleme
# psycopg2'nin Alpine Linux'ta doğru çalışması için gerekli bağımlılıklar
# build-base: C derleyici ve diğer derleme araçları
# libpq-dev: PostgreSQL istemci kütüphaneleri (psycopg2 için gerekli)
# linux-headers: Bazı Python paketlerinin derlenmesi için gerekli
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --no-cache build-base libpq-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del build-base libpq-dev linux-headers && \
    apk add --no-cache postgresql-client && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]