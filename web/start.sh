#!/bin/sh
django-admin createsuperuser --noinput --username admin
python manage.py collectstatic --noinput
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn web.wsgi --bind=unix:/tmp/stream/gunicorn.sock --workers=1

