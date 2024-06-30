from db import DB
import logging
import datetime
import time
import randomname
from pymongo.cursor import CursorType

def subscribe(db: DB, freq: int):
    """
    Subscribe to messages from the capped collection. Logs the received message and also prints it out
        
    :param db.DB db: the handle to the MongoDB database
    :param freq: number of seconds to wait between two polling attempts    
    """

    logger = logging.getLogger(__name__)
    collection = db.get_collection()

    cur = collection.find(cursor_type=CursorType.TAILABLE_AWAIT)
    for i in range(100):
        for msg in cur:
            logger.info(f"Subscribe run #{i}, received msg: {msg}")

        time.sleep(freq)