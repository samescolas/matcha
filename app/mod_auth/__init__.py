from flask import Blueprints
from views import *

mod_auth = Blueprint('auth', __name__, template_folder="templates")
