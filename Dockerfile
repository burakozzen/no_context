FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . ./app/no_context

CMD ["uvicorn","hello_world_app.hello_world_app:app","--host","0.0.0.0","--port","8000"]