import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mflix"]

movies = db["movies"]

pipeline = [
    {'$unwind': '$languages'},
    {'$group': {'_id': '$languages', 'count': {'$sum': 1}}}
]

result = db.movies.aggregate(pipeline)
for doc in result:
    print(doc['_id'], doc['count'])