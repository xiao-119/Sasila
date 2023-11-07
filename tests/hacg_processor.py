import base

from bs4 import BeautifulSoup as bs4
from requests import Response
from sasila.downloader.http.spider_request import Request
from sasila.processor.base_processor import BaseProcessor
from sasila.spider.core import SpiderCore

# 解析HTML


class HACG_Processor(BaseProcessor):
    def __init__(self):
        self.start_requests = [
            Request(url="https://www.hacg.lv/wp/anime.html", callback=self.process)
        ]
        
        
        self.data = []


    def process(self, response:Response):
        print(response.status_code)
        # print(response.text)
        soup = bs4(response.content, 'html.parser', from_encoding='utf-8')
        articles = soup.find_all('article')
        for article in articles[:]:
            title = article.select('a[rel="bookmark"]')[0].text
            if title == '':
                continue
            href = article.select('a[rel="bookmark"]')[0]['href']
            
            aaa = article.select('div.comments-link a')
            # print(aaa)
            cnt = article.select('div.comments-link a')[0].text
            
            print(cnt, title, href)
            
            
        return "Request(callback=self.process_title)"
    

    def process_title(self, response):
        pass

if __name__ == "__main__":
      SpiderCore(HACG_Processor()).start()
