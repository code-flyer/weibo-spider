from aip import AipNlp
import time
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from dbaccess import readdatabase
from writetodb import writedb
APP_ID = '17666412'
API_KEY = 'vvXYCbFdamtuc7yMWidy0lrV'
SECRET_KEY = 'YlhubBQuy4Y3Ghr9IxVVF8Nl6EkvMH7v'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def decision():
    data = readdatabase('weibo_text')
    for remark in data:
        result=client.sentimentClassify(remark)
        time.sleep(0.4)
        # print(result)
        if 'items' in result.keys():
            emotion = result['items'][0]
            if emotion['positive_prob'] > emotion['negative_prob']:
                emotion_value = emotion['positive_prob']
            else:
                emotion_value = emotion['negative_prob']
        values={
            'emotion':emotion_value,
        }
        table1=writedb()
        table1.insert_one(values)
        print(values)
    
def piechart():
    positive=0
    negative=0
    neutral=0
    data1 = readdatabase('emotion','emotion_values')
    for value in data1:
        if value>=0.8:
            positive=positive+1
        elif value<=0.6:
            negative=negative+1
        else:
            neutral=neutral+1
    posi_perc = positive/len(data1)
    nega_perc = negative/len(data1)
    neutral_perc = neutral/len(data1)
    font = FontProperties(fname=r'C:\Users\ThinkPad\Desktop\NLP\Alibaba-PuHuiTi-Medium.ttf',size=14)
    data_set=[nega_perc,posi_perc,neutral_perc]
    labels=["Negative","Positive","Neutral"]
    plt.axes(aspect='equal')
    plt.xlim(0,8)
    plt.ylim(0,8)
    plt.pie(x=data_set,
    explode=[0.5,0.5,0],
    labels=labels,
    autopct='%.3f%%',
    pctdistance=0.8,
    labeldistance = 1.15,
    startangle = 180,
    center = (4, 4),
    radius = 3.8,
    counterclock = False,
    wedgeprops = {'linewidth': 1, 'edgecolor':'green'},
    textprops = {'fontsize':12, 'color':'black'},
    frame = 1)
    plt.xticks()
    plt.yticks()
    plt.title('情感分析分布',fontproperties=font)
    plt.show()

#decision()
piechart()