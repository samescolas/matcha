FROM debian:wheezy

ENV APP_DIR /usr/src/matcha
ENV FLASK_APP $APP_DIR/run.py

RUN mkdir -p $FLASK_APP
COPY ./ $FLASK_APP

RUN cp $FLASK_APP/.[vb]* /root/

RUN apt-get update && apt-get upgrade && apt-get install -y \
	python3 \
	python-pip \
	git \
	vim

RUN pip install Flask && pip install Flask-PyMongo && pip install flask_wtf

ENTRYPOINT bash
