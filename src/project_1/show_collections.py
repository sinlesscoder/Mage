from pymongo import MongoClient

uri='104.225.217.176:8363'

client = MongoClient(uri)

db = client['aliexpress_items']

# See all the collections
db.