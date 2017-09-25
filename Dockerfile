FROM debian:latest

ENV APP_DIR /var/www/matcha
ENV FLASK_APP $APP_DIR/run.py

RUN mkdir -p $APP_DIR
COPY ./ $APP_DIR

RUN cp $APP_DIR/.[vb]* /root/

RUN apt-get update && apt-get install -y \
	apache2 \
	curl \
	libapache2-mod-wsgi \
	mysql-server \
	python3 \
	python-mysqldb \
	python-pip \
	git \
	vim

WORKDIR /var/www/matcha

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN service mysql start && \
	mysqladmin -u root password matcha && \
	mysqladmin create matcha && \
	mysql -u root -e "$(cat $APP_DIR/config.sql)"

RUN curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && \
	chmod a+x nodesource_setup.sh && \
	/bin/bash nodesource_setup.sh && \
	rm nodesource_setup.sh && \
	apt-get install -y nodejs && \
	npm install -g npm && \
	npm install -g bower && \
	bower install bower.json && \
	mv bower_components static/bower_components

ENTRYPOINT bash
