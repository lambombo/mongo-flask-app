from flask import jsonify
from flask_restful import Resource
from .api_util import build_domain_response

from .. import mongo
from . import api_ext


class hosts(Resource):
    def get(self):
        hosts = mongo.db.hosts
        output = []
        for s in hosts.find():
            output.append(build_domain_response(s))
        return jsonify({'data' : output})

api_ext.add_resource(hosts, "/dump", endpoint = "hosts")
