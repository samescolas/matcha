from flask import Blueprint, render_template

register = Blueprint('register', __name__, template_folder="templates")

@register.route('/')
def register_page():
	return render_template('register.html')
