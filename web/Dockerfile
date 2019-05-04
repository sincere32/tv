FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /django
COPY . /django/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN chmod +x /django/start.sh
ENTRYPOINT /django/start.sh
