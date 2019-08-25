FROM python:3.7.4-alpine
RUN apk --update-cache \
    add curl \
    tzdata \
    fontconfig && \
    cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

WORKDIR /home

COPY . /home
RUN pip install pipenv && \
    pipenv install

EXPOSE 8080
CMD ["pipenv", "run", "python", "run.py"]
