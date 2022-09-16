FROM python:3.8-slim-buster

WORKDIR /usr/app

COPY . .

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "./start.sh"]

CMD ./start.sh
