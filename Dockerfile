FROM node:boron

WORKDIR /usr/src/matcha

COPY package.json .

RUN npm install
RUN apt-get update && apt-get install -y vim

COPY .git .git
COPY .vimrc /root/.vimrc
COPY .bashrc /root/.bashrc
COPY . .

EXPOSE 8080

CMD [ "bash" ]
# CMD [ "npm", "start" ]
