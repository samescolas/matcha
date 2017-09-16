from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return 'Hello, world!'

@app.route('/login/?', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template( 'login.html', 
				title='Sign In', 
				form=form)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404
