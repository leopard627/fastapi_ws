FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y software-properties-common \
  build-essential checkinstall \
  postgresql postgresql-contrib \
  build-essential \
  libpq-dev gcc \
  git \
  nginx \
  supervisor \
  sqlite3 \
  locales && \
  rm -rf /var/lib/apt/lists/*

# install python3.11
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt install -y python3.11-distutils \
  python3.11 \
  python3-dev \
  python3-pip \
  libpython3.11-dev

WORKDIR /project

RUN python3.11 -m pip install -U pip setuptools

ADD requirements/requirements.txt /project/

RUN python3.11 -m pip install -r /project/requirements.txt

RUN python3.11 -m pip install --upgrade pip setuptools

ADD . /project/

ENV DATABASE_CONFIG=${DATABASE_CONFIG} \
  REDIS_URL=${REDIS_URL}

EXPOSE 443
EXPOSE 80

CMD ["uvicorn", "fastapi_ws.main:app", "--host", "0.0.0.0", "--port", "8000", "--ws-ping-timeout", "300", "--timeout-keep-alive", "300", "--ws-ping-interval", "300"]
