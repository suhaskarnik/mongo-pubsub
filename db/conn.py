from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from dotenv import load_dotenv
from os import environ
import logging 

COLL_NAME = "messages"
DB_NAME = "chat"

logger = logging.getLogger(__name__)

class DB:
    def __init__(self):
        load_dotenv()

        CONN_STR = environ.get("MONGO_URL")

        logger.info(f"Connecting to Mongo DB at URL: {CONN_STR}")
        # CONN_STR = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.10"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONN_STR)

        # Create the database for our example
        self.db = client[DB_NAME]
    
    def init_coll(self, size=1000):
        if COLL_NAME in self.db.list_collection_names() : 
            self.db.drop_collection(COLL_NAME)
        
        self.db.create_collection(COLL_NAME, capped=True, size=size)


    def get_db(self) -> Database:
        return self.db
    
    def get_collection(self) -> Collection:
        collection = self.db[COLL_NAME]
        return collection