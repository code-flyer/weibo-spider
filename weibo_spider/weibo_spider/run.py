from scrapy.cmdline import execute

def startcrawl():
    execute("scrapy crawl weibo ".split())

def main():
    startcrawl()
if __name__ == '__main__':
    main()