FROM python:2.7

ADD . /mongo_app_api
WORKDIR /mongo_app_api

RUN pip install -q -r requirements.txt
CMD python manage.py runserver --host 0.0.0.0 --port 5000
