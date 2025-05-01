FROM python:3.10-slim-buster

WORKDIR /webhook

COPY ./app/* /webhook/

RUN pip install --no-cache-dir --upgrade -r /webhook/requirements.txt

CMD ["./gunicorn.sh"]