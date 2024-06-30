from db import DB
import logging
import datetime
import time
import randomname


def publish(db: DB, nouns: list[str], freq: int):
    """
    Publish messages to the capped collection. Logs the published message and also prints it out
        
    :param db.DB db: the handle to the MongoDB database
    :param list[str] nouns: each message will contain random real words, to easily distinguish messages. `nouns` controls the classes of words. Optionally pass one or more values from the nouns listed here: https://pypi.org/project/randomname/ 
    :param freq: number of seconds to wait between two messages    
    """
    logger = logging.getLogger(__name__)
    collection = db.get_collection()

    for i in range(100):
        if len(nouns) > 0:
            name = randomname.get_name(noun=tuple(nouns))
        else:
            name = randomname.get_name()

        msg = {
        "text" : f"Chat Message {i}: {name}",
        "ts" : datetime.datetime.now() 
        }
        collection.insert_one(msg)
        logger.info(f"message {i} written: {name}")

        time.sleep(freq)