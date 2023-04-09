import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mflix"]
comments_collection = db["comments"]
movies_collection = db["movies"]


movie = movies_collection.find_one({"title": "The Taking of Pelham 1 2 3"})

commenters = set()
for comment in comments_collection.find({"movie_id": movie["_id"]}):
    commenters.add(comment["name"])


print("People who commented on '{}' movie:".format(movie["title"]))
for commenter in commenters:
    print(commenter)
