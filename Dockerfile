FROM python:3.7-alpine

ENV PYTHONUNBUFFERED0=1

# install requirements using pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# using the right dir
RUN mkdir /app
WORKDIR /app 
COPY ./app /app

# the right user for security perposes
RUN adduser -D user
USER user