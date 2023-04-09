import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['mflix']
collection = db['movies']

pipeline = [
    {'$unwind': '$languages'},
    {
        '$group': {
            '_id': '$languages',
            'avg_rating': {'$avg': '$imdb.rating'}
        }
    }
]

result = collection.aggregate(pipeline)
for doc in result:
    print(f"Language: {doc['_id']}, Average IMDB rating: {doc['avg_rating']}")
