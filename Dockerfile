FROM python:3.10-slim-buster
WORKDIR /webhook
COPY requirements.txt /webhook
COPY app.py /webhook

RUN pip install --no-cache-dir --upgrade -r /webhook/requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000","--cert=/certs/tls.crt", "--key=/certs/tls.key"]

#CMD gunicorn --certfile=/certs/tls.crt --keyfile=/certs/tls.key --bind 0.0.0.0:443 wsgi:webhook

#CMD ["uvicorn", "app.py", "--host", "0.0.0.0", "--port", "8080","--ssl-keyfile=/certs/tls.key", "--ssl-certfile=/certs/tls.crt"]