FROM python:3.10

RUN mkdir /app

COPY requirements.txt /app
COPY app.py /app
COPY model /app/model
COPY predict /app/predict
COPY preprocessing /app/preprocessing

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn app:app --host 0.0.0.0 
