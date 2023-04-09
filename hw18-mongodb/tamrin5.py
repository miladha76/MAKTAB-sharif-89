import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mflix"]

movies = db["movies"]

pipeline = [
    {"$sort": {"num_mflix_comments": -1}},
    {"$limit": 1},
    {"$project": {"_id": 0, "title": 1}}
]

result = db.movies.aggregate(pipeline)

for doc in result:
    print(doc['title'])
