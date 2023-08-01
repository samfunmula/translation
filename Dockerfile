FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN apt update && \
    pip install --no-cache-dir -r requirements.txt

RUN pip install fastapi
RUN pip install fasttext
RUN pip install torch

COPY main .

EXPOSE 9321

CMD python3 api.py
