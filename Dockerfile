FROM python:3.6.9-alpine

RUN apk --update-cache \
    add curl \
    tzdata \
    gcc \
    git \
    libc-dev \
    libxml2-dev \
    fontconfig \
    mesa-gl \
    glu \
    libxslt-dev && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

RUN pip install emojilib --extra-index-url https://repo.fury.io/emoji-gen/

