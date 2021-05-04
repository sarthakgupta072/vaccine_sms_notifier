FROM python:3.9-slim-buster

LABEL maintainer.name = "Sarthak Gupta"
LABEL maintainer.email="sarthakgupta072[at]gmail[dot]com"

# Install general dependencies
ENV PACKAGES python3-dev cron 
RUN apt-get update && \
    apt-get install -y --no-install-recommends ${PACKAGES} && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./


RUN pip install \
        --no-warn-script-location \
        -r requirements.txt

COPY ./ /app


RUN chmod +x /app/entrypoint.sh

ENTRYPOINT /app/entrypoint.sh
