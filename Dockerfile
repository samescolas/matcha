FROM debian:wheezy

ENV APP_DIR /usr/src/matcha
ENV FLASK_APP $APP_DIR/run.py

RUN mkdir -p $APP_DIR
COPY ./ $APP_DIR

RUN cp $APP_DIR/.[vb]* /root/

RUN apt-get update && apt-get upgrade && apt-get install -y \
	apache2 \
	libapache2-mod-wsg \
	mysql-client \
	mysql-server \
	python3 \
	python-pip \
	git \
	vim

RUN pip install Flask && pip install Flask-PyMongo && pip install flask_wtf

ENTRYPOINT bash
