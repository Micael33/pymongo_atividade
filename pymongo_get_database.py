from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['clinica']

if __name__ == "__main__":
    dbname = get_database()