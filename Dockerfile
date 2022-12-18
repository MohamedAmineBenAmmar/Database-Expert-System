FROM python:3.8

WORKDIR /DB_Expert_System

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./app ./app

COPY database_expert_system.py ./database_expert_system.py

CMD ["python", "./database_expert_system.py"]