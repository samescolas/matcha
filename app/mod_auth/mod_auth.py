from flask import Blueprint, render_template

login = Blueprint('login', __name__, template_folder="templates")
register = Blueprint('register', __name__, template_folder="templates")

@login.route('/')
def login_page():
	return render_template('login.html')

@register.route('/')
def register_page():
	return render_template('register.html')
