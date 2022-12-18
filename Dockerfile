FROM python:3.8

WORKDIR /DB_Expert_System

COPY ./backend/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./backend/app ./app

CMD ["python", "./app/main.py"]