from pymongo import MongoClient
import datetime
import random
import copy
client = MongoClient('mongodb://localhost:27017/')
db = client['mongo_db_lab']
collection = db['mongo_db_lab.collection']
definitions = db.definitions


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    definitions_list = []
    for definition in definitions.find():
        definitions_list.append(definition)
    # print(definitions_list)
    random_word = random.choice(definitions_list)
    random_word_new = copy.deepcopy(random_word)
    timestamp = datetime.datetime.utcnow()
    timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    if "dates" in random_word:
        random_word_new["dates"].append(timestamp)
    else:
        random_word_new["dates"] = [timestamp]
    definitions.update_one(random_word, {"$set": random_word_new})
    return random_word_new


if __name__ == '__main__':
    print(random_word_requester())
