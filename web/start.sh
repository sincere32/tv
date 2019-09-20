#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --password admin --email foo@foo.foo
python manage.py collectstatic --noinput
gunicorn web.wsgi --bind=unix:/tmp/stream/gunicorn.sock --workers=1

