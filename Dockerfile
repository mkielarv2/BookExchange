FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /djangoBookExchange
WORKDIR /djangoBookExchange
ADD . /djangoBookExchange

RUN apt-get update
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/djangoBookExchange/manage.py", "runserver", "0.0.0.0:8000"]
