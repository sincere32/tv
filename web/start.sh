#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn web.wsgi --bind=unix:/tmp/stream/gunicorn.sock --workers=1

