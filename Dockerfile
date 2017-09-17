FROM debian:latest

ENV APP_DIR /var/www/matcha
ENV FLASK_APP $APP_DIR/run.py

RUN mkdir -p $APP_DIR
COPY ./ $APP_DIR

RUN mv $APP_DIR/.[vb]* /root/

RUN apt-get update && apt-get upgrade && apt-get install -y \
	apache2 \
	libapache2-mod-wsgi \
	mysql-server \
	python3 \
	python-pip \
	git \
	vim

RUN pip install Flask && pip install Flask-PyMongo && pip install flask_wtf

RUN service mysql start && \
		mysqladmin -u root password matcha && \
		mysqladmin create matcha && \
		mysql -u root -e "$(cat $APP_DIR/init.sql)"

ENTRYPOINT bash
