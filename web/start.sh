#!/bin/sh
python manage.py collectstatic --noinput
gunicorn web.wsgi --bind=unix:/tmp/stream/gunicorn.sock --workers=1

