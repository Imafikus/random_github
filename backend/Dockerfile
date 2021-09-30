FROM python:3.9-slim

RUN mkdir /home/random-github-server
WORKDIR /home/random-github-server

COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY main.py .
COPY models.py .
COPY datastore_db.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
