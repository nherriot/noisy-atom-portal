#Pull official base image for Python 3.8
FROM python:3.8-slim-buster

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

#Create a working directory
WORKDIR /app

#First parameter tells docker which files to copy to the docker file, second parameter location to copy to
COPY requirements.txt requirements.txt

#Execute the command and install all required packages
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Add source code to the image
COPY . /app/

#Expose the port the server is running on
EXPOSE 8000

#Run the command to runserver
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
