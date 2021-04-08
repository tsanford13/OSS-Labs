from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId
if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mongo_db_lab']
    collection = db['mongo_db_lab.collection']
    print(db.list_collection_names())
    definitions = db.definitions
    
    # fetch all definitions
    for definition in definitions.find():
        pprint.pprint(definition)
        
    # fetch one definition
    pprint.pprint(definitions.find_one())
    
    # fetch one definition based on query
    pprint.pprint(definitions.find_one({"word": 'Zoomie'}))
    
    # fetch one definition based on id
    pprint.pprint(definitions.find_one({"_id": ObjectId('56fe9e22bad6b23cde07b8ba')}))
    
    # insert a new record
    definition = {"word": "yolo", "definition": "to yolo means to do something risky for fun, because you only live once!"}
    definition_id = definitions.insert_one(definition).inserted_id
    pprint.pprint(definitions.find_one({"word": "yolo"}))
