from sasila.downloader.http.spider_request import Request
from sasila.downloader.requests_downloader import RequestsDownLoader
from sasila.processor.base_processor import BaseProcessor
from typing import List

class SpiderCore(object):
    def __init__(self, processor: BaseProcessor):
        # self.spider = spider
        # self.settings = spider.settings
        # self.scheduler = Scheduler(spider)
        self.scheduler: List[Request] = []
        self.downloader = RequestsDownLoader()
        # self.pipeline = Pipeline(spider)
        # self.spider_task = SpiderTask(spider)
        # self.spider_task.add_task(spider.start_urls)
        self.scheduler.extend(processor.start_requests)

    def _crawler(self):
        while self.scheduler:
            request = self.scheduler.pop(0)
            res = self.downloader.download(request)
            res_call = request.callback(res)
            if isinstance(res_call, Request):
                self.scheduler.append(res_call)
            elif isinstance(res_call, List):
                print("item",request.url)
    def start(self):
        self._crawler()
