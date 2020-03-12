# -*- coding: utf-8 -*-
import scrapy
import json
import re,time,logging


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['http://m.weibo.cn/']
    base_url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D{}&page_type=searchall'
    search_key = input("please input the keywords:")
    url = base_url.format(search_key)


    def start_requests(self):
        cookies = {'_T_WM' : '17092794410',
        'WEIBOCN_FROM' : '1110006030',
        'SUB' : '_2A25wdifQDeRhGeVK4lUT8inNwj6IHXVTmUmYrDV6PUJbkdANLVXdkW1NTDEpLzQcaTJkB_nSZ2JqrRHm5VLSQrav',
         'SUHB' : '0N2F7mxJEpc2tE',
        'MLOGIN' : '1',
        'XSRF-TOKEN' : '51a430',
        'M_WEIBOCN_PARAMS' : 'lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174'
        }
        yield scrapy.Request(self.url, callback=self.parse, dont_filter=False,cookies=cookies)

    def parse(self, response):
        results = json.loads(response.text)
        if results.get('ok') and results.get('data').get('cards'):
            details = results.get('data').get('cards')
            for detail in details:
                mblog = detail.get('mblog')
                if mblog:
                    contents={}
                    created_time = mblog.get('created_at')
                    if re.match('刚刚', created_time):
                        created_time = time.strftime('%Y-%m-%d %H:00', time.localtime(time.time()))
                    elif re.match('\d+分钟前', created_time):
                        minute = re.match('(\d+)', created_time).group(1)
                        created_time = time.strftime('%Y-%m-%d %H:00', time.localtime(time.time() - float(minute) * 60))
                    elif re.match('\d+小时前', created_time):
                        hour = re.match('(\d+)', created_time).group(1)
                        created_time = time.strftime('%Y-%m-%d %H:00', time.localtime(time.time() - float(hour) * 60 * 60))
                    elif re.match('昨天.*', created_time):
                        created_time = re.match('昨天(.*)', created_time).group(1).strip()
                        created_time = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(24 * 60 * 60)))+''+created_time
                    else:
                        created_time = time.strftime('%Y-', time.localtime()) + created_time
                    contents["created_time"] = created_time
                    raw_text = mblog.get('text')
                    clean_text=re.sub('<[^>]+>','',raw_text)
                    contents['weibo_text'] = clean_text
                    contents["created_by"] = mblog.get('user').get('screen_name')
                    contents["reposts_count"] = mblog.get('reposts_count')
                    contents["comments_count"] = mblog.get('comments_count')
                    contents["thumb"] = mblog.get('attitudes_count')
                    contents["link_url"] = detail.get('scheme')
                    print(contents)
                    yield contents


        next_urls = self.url + '&page={}'
        for page in range(2,55):
            next_url = next_urls.format(page)
            yield scrapy.Request(next_url, callback=self.parse)

