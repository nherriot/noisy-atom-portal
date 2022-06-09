#Pull official base image for Python 3.8
FROM python:3.8-slim-buster

RUN mkdir -p /app/
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#RUN apt-get install libpq-dev python-dev python3.8-dev 
#RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
