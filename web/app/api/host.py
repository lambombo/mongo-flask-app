from flask import jsonify
from flask_restful import Resource
from .api_util import build_domain_response#, MongoJSONEncoder
from .. import mongo
from . import api_ext


class host(Resource):
    def get(self, id):
        host = mongo.db.hosts
        output = []
        s = host.find_one_or_404({"id": id})
        output.append(build_domain_response(s))
        return jsonify({'data': output})

api_ext.add_resource(host, "/id/<int:id>", endpoint = "host")
