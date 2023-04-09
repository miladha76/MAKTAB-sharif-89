import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client["mflix"]

movies = db["movies"]


history_movies = movies.find({"genres": {"$in": ["History"]}})

for movie in history_movies:
    print(movie["title"])
