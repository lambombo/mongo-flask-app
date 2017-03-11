from pymongo import MongoClient
import json

with open('init_db.json') as f:
    data = json.loads(f.read())

client = MongoClient('192.168.99.100', 27017)

db = client.hosts

hosts = db.hosts

hosts = hosts.insert_many(data)
