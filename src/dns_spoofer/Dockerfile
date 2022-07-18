FROM python:2.7-buster

RUN apt-get update && apt-get install -y python-pip build-essential python-dev libnetfilter-queue-dev

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["python", "dns_spoofer.py"]