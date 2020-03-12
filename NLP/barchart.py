from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from collections import Counter
from dbaccess import readdatabase



def plot():
    column='created_time'
    data=readdatabase(column)
    fileobj = open(r'C:\Users\ThinkPad\Desktop\NLP\time.txt','a',encoding='UTF-8')
    for line in data:
        fileobj.write(line+'\n')
    #print(line)
    fileobj.close()
    file = open(r'C:\Users\ThinkPad\Desktop\NLP\time.txt','r',encoding='UTF-8')
    list1=file.readlines()
    time_freq=Counter(sorted(list1))
    time=[i for i in time_freq.keys()]
    freq=[j for j in time_freq.values()]
    c = (
            Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(time)
            .add_yaxis("日均访问量",freq)
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
            title_opts=opts.TitleOpts(title="微博话题访问量分布"),       
            )
        )
    c.render()
plot()