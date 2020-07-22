FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libc6-dev-i386 \
    python3 \
    python3-dev \
    python3-pip \
    mysql-server \
    libmysqlclient-dev \
    curl \
    net-tools \
    htop \
    curl \
    wget \
    iproute2
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r /code/requirements.txt