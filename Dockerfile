FROM python:3.6.9-slim-stretch

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install pytype
RUN pip3 install mypy

WORKDIR /app

COPY ./sandbox /app

CMD ["sleep", "9999999"]
