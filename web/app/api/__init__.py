from flask import Blueprint, current_app, render_template
from flask_restful import Api

from .. import app

api = Blueprint('api', __name__)
api_ext = Api(api)

@api.route("/", methods=["GET"])
def index():
    return render_template('api_base.html'), 200

from . import hosts, host
