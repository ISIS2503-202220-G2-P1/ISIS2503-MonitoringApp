FROM python:3

WORKDIR /usr/app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ./start.sh
