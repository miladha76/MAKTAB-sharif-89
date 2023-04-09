import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mflix"]

movies = db["movies"]

query = {"year": {"$gte": 1990, "$type": "int"}, "imdb.rating": {"$exists": True}}

for movie in movies.find(query):
    print(f"{movie['title']}: {movie['imdb']['rating']}")
