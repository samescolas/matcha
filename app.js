'use strict'

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();

// Define header
app.all('/*', function (req, res, next) {
	res.msg = '<h1>Matcha</h1>';
	next();
});

app.get('/', (req, res) => {
	res.send(res.msg + '<h1>hello, world!</h1>');
});

app.get('/about', (req, res) => {
	res.send(res.msg + '<h1>About</h1>');
});

app.get('/testing', (req, res) => {
	res.send(res.msg + 'Testing page');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
