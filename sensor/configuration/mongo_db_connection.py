import pymongo
import os
import sys
import certifi
from sensor.constant.database import DATABASE_NAME
from  sensor.exception import SensorException


ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                
                mongo_db_url ="mongodb+srv://shiva:12345@cluster0.ntojkjj.mongodb.net/test"
                #mongo_db_url="mongodb+srv://avnish:Aa327030@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"
                #mongodb+srv://avnish:Aa327030@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client

            self.database = self.client[database_name]

            self.database_name = database_name

        except Exception as e:
            raise SensorException(e, sys)
