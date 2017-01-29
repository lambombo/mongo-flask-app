import json
from bson import ObjectId

def build_domain_response(s):
    d = {'street':s['street'],
        'lat': s['lat'],
        'long':s['long'],
        'country':s['country'],
        'city':s['city'],
        'id':s['id'],
        'domain':s['domain']}

    #d = {i:s[i] for i in s}
    return d


class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return (self, o)
