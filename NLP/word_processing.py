import jieba
import csv
import pandas as pd
from dbaccess import readdatabase


#将分词结果写入到result.txt中
def wordcut():
    column='weibo_text'
    data = readdatabase(column)
    for remark in data:
        stopping_words = pd.read_csv(r'C:\Users\ThinkPad\Desktop\NLP\stopping_words.txt',encoding='UTF-8',names=['w'])
        newlist = [word for word in jieba.lcut(remark) if word not in list(stopping_words.w)]
        result = open(r'C:\Users\ThinkPad\Desktop\NLP\result.txt','a',encoding='UTF-8')
        result.write(str(newlist).replace('[','').replace(']','').replace("'",'').strip())
        result.close()
        print("succeed")


wordcut()



    