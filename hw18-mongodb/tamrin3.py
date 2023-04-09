import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mflix"]

movies = db["movies"]

query = {"$and": [{"year": {"$gte": 1990}}, {"$or": [{"year": {"$type": "int"}}, {"year": {"$type": "string"}}]}, {"imdb.rating": {"$exists": True}}]}

for movie in movies.find(query):
    print(f"{movie['title']}: {movie['imdb']['rating']}")
