import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mflix"]
collection = db["movies"]

pipeline = [
    {"$unwind": "$cast"},
    {"$group": {"_id": "$cast", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]

result = collection.aggregate(pipeline)

for doc in result:
    print(f"{doc['_id']}: {doc['count']}")
