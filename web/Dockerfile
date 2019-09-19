FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /django
COPY . /django/
RUN pip install -r requirements.txt
RUN chmod +x /django/start.sh
ENTRYPOINT /django/start.sh
