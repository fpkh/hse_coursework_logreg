FROM ubuntu:latest
MAINTAINER Fedor Pakhurov 'pahurov04@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app 
RUN pip install -r flask/requirements.txt
ENTRYPOINT ["python3"]
CMD ["flask/app.py"]