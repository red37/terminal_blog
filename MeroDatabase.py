import pymongo


class MeroDatabase(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None  # test1

    # COLLECTION??

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(MeroDatabase.URI)
        MeroDatabase.DATABASE = client['test1']

    @staticmethod
    def insert(collection, data):
        MeroDatabase.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return MeroDatabase.DATABASE[collection].find(query)  # gives cursor object

    @staticmethod
    def find_one(collection, query):
        return MeroDatabase.DATABASE[collection].find_one(query)  # gives the required element
