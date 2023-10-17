FROM python:3.10

ENV PYTHONUNBUFFERED=0

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./src/* /app/

EXPOSE 8000

CMD [ "uvicorn", "main:flixfinder", "--host", "0.0.0.0", "--port", "8000" ]