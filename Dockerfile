FROM python:3.10

ADD hello_world_main.py .

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","./hello_world_main.py"]