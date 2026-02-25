# En güncel stabil Python Alpine sürümü
FROM python:3.12-alpine

LABEL maintainer="emrefikirlier@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

# GÜNCELLEME NOTLARI:
# 1. gettext eklendi (i18n desteği için zorunlu)
# 2. libffi-dev eklendi (Bazı kripto ve auth paketleri için gerekebilir)
# 3. jpeg-dev, zlib-dev vb. (Pillow'un tam performanslı çalışması için alpine'de önerilir)

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Derleme araçlarını yükle
    apk add --no-cache --virtual .build-deps \
        build-base \
        postgresql-dev \
        musl-dev \
        linux-headers \
        libffi-dev \
        jpeg-dev \
        zlib-dev && \
    # Çalışma zamanı araçlarını yükle (Bunlar silinmeyecek)
    apk add --no-cache \
        postgresql-client \
        gettext \
        libjpeg-turbo \
        libpng && \
    /py/bin/pip install -r /requirements.txt && \
    # Gereksiz derleme araçlarını temizle (Konteyner boyutu için)
    apk del .build-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]