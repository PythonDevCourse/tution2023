FROM python:3.9-bullseye as python
MAINTAINER Peter A. Kurishev <peter@kurishev.ru>

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /var/www

WORKDIR /var/www

ENTRYPOINT ["python","manage.py", "runserver", "0.0.0.0:8000"]
