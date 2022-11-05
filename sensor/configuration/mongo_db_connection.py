import os
import sys
import certifi
import pymongo
from sensor.constants import DATABASE_NAME

ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("mongodb+srv://shiva:12345@cluster0.ntojkjj.mongodb.net/test")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client

            self.database = self.client[database_name]

            self.database_name = database_name

        except Exception as e:
            raise SensorException(e, sys)
