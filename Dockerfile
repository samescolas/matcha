FROM debian:wheezy

ENV APP_PATH /usr/src/app

RUN mkdir -p $APP_PATH
COPY ./ $APP_PATH

RUN cp $APP_PATH/.[vb]* /root/

RUN apt-get update && apt-get upgrade && apt-get install -y \
	python3 \
	python-pip \
	git \
	vim

RUN pip install Flask && pip install Flask-PyMongo && pip install flask_wtf

ENTRYPOINT bash
