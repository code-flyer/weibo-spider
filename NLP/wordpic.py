import nltk
from nltk import FreqDist
import wordcloud
import matplotlib.pyplot as plt

def picture():  #词云绘制
    file = open(r'C:\Users\ThinkPad\Desktop\NLP\result.txt','r',encoding='UTF-8')
    result =''
    for i in file:
        result = result+i
        result = result.replace(' ','').split(',')
    fdist = nltk.FreqDist(result)
    wordcount = dict(fdist.items())
    myfont=r'C:\Users\ThinkPad\Desktop\NLP\Alibaba-PuHuiTi-Medium.ttf'
    cloudobj=wordcloud.WordCloud(font_path=myfont,width=1200,height=800,
                            mode="RGBA",background_color=None).fit_words(wordcount)
    plt.imshow(cloudobj)
    plt.axis("off")
    plt.show()
    cloudobj.to_file(r'C:\Users\ThinkPad\Desktop\NLP\pic.png')

picture()