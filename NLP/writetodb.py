import pymongo
import pandas as pd

def writedb(tb='emotion_values'):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['scrapy_db']
    table = db[tb]
    return table