#!/bin/sh
gunicorn --certfile=/certs/tls.crt --keyfile=/certs/tls.key  wsgi:app -w ${WORKERS:-2} --threads ${THREADS:-2} -b 0.0.0.0:8080