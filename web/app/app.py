from flask import Flask, jsonify, request, render_template, Blueprint
from .domain import get_domain

main = Blueprint('main', __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template('main/index.html'), 200

# @main.route("/domain_entry", methods=["GET"])
# def domain_entry():
#     return ('get_domain page')

# @main.route("/get_info/<url>",  methods=["GET"])
# def domain(url):
#     return render_template('get_info_domain.html', data = jsonify(get_domain(url)))


@main.route("/get_info/", methods=["GET"])
def get_info():
    return render_template('get_info/index.html')

@main.route("/get_map/", methods = ["GET"])
def get_map():
    return render_template('get_map/index.html'), 200
