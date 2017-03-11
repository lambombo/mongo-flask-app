from flask import Flask, jsonify, request, render_template, Blueprint
from .domain import get_domain

main = Blueprint('main', __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template('main/index.html'), 200
