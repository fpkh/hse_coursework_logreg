# FROM ubuntu:latest
# MAINTAINER Fedor Pakhurov 'pahurov04@gmail.com'
FROM python:3.9
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app 
RUN pip3 install --upgrade pip -r flask/requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["flask/app.py"]
