from bson import ObjectId
from pymongo import MongoClient
from utils.config import MONGODB_CONNECTION_STRING

client = MongoClient(MONGODB_CONNECTION_STRING)

db = client["cosmo_assignment"]

collection_products = db["products"]
collection_orders = db["orders"]


def serialize_data(data):
    data = list(data)
    for item in data:
        if "_id" in item and isinstance(item["_id"], ObjectId):
            item["id"] = str(item["_id"])
            del item["_id"]
    return data
