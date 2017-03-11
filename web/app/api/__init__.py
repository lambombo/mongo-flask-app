from flask import Blueprint, render_template
from flask_restful import Api


api = Blueprint('api', __name__)
api_ext = Api(api)

@api.route("/", methods=["GET"])
def index():
    return render_template('api/api_base.html'), 200

from . import hosts, host
