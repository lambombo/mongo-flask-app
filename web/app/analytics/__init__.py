from flask import Blueprint, current_app, render_template


analytics = Blueprint('analytics', __name__)

@analytics.route("/", methods=["GET"])
def index():
    return render_template('analytics/index.html'), 200

@analytics.route("/get_info/", methods=["GET"])
def get_info():
    return render_template('analytics/get_info.html')

@analytics.route("/get_map/", methods = ["GET"])
def get_map():
    return render_template('analytics/get_map.html'), 200
