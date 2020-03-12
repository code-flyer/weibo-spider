import pymongo
import pandas as pd

def readdatabase(column,tb='weibo_content'):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['scrapy_db']
    table = db[tb]
    data = pd.DataFrame(list(table.find()))
    data = data[column]
    return data