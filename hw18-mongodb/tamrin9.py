import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['mflix']  

pipeline = [
    {"$unwind": "$cast"},
    {"$group": {
        "_id": {"actor": "$cast", "genre": "$genres"}
    }},
    {"$group": {
        "_id": "$_id.actor",
        "genres": {"$addToSet": "$_id.genre"}
    }},
    {"$sort": {"_id": 1}}
]

result = db.movies.aggregate(pipeline)

for doc in result:
    actor = doc['_id']
    genres = doc['genres']
    if genres:  
        genre_str = ', '.join(list(set([genre for sublist in genres for genre in sublist])))
        print(actor + ': ' + genre_str)
