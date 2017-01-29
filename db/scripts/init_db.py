from pymongo import MongoClient
import json

with open('host_list.json') as f:
    data = json.loads(f.read())


client = MongoClient('localhost', 27017)

db = client.hosts

hosts = db.hosts

hosts = hosts.insert_many(data)
