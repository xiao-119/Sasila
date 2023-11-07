import requests
from bs4 import BeautifulSoup
from sasila.downloader.base_downloader import BaseDownLoader
from sasila.downloader.http.spider_request import Request


class RequestsDownLoader(BaseDownLoader):
    def __init__(self):
        self._headers = dict()
        self._headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        self._headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        self._headers["Accept-Encoding"] = "gzip, deflate, sdch"
        self._headers["Accept-Language"] = "zh-CN,zh;q=0.8"
        
        
        
    def download(self, request:Request):
        response = requests.get(request.url)
        return response
