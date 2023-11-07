import base

from bs4 import BeautifulSoup as bs4
from requests import Response
from sasila.downloader.http.spider_request import Request
from sasila.processor.base_processor import BaseProcessor
from sasila.spider.core import SpiderCore

# 解析HTML


class HACG_Processor(BaseProcessor):
    data = []

    def __init__(self):
        self.start_requests = [
            Request(url="https://www.hacg.lv/wp/anime.html", callback=self.process)
        ]

        for i in range(2, 151):
            self.start_requests.append(
                Request(
                    url="https://www.hacg.lv/wp/anime.html/page/%d" % i,
                    callback=self.process,
                )
            )

    def process(self, response: Response):
        print(response.status_code)
        # print(response.text)
        soup = bs4(response.content, "html.parser", from_encoding="utf-8")
        articles = soup.find_all("article")
        for article in articles[:]:
            title = article.select('a[rel="bookmark"]')[0].text
            if title == "":
                continue
            href = article.select('a[rel="bookmark"]')[0]["href"]

            datetime = article.select("time")[0]["datetime"]
            cnt = article.select("div.comments-link a")[0].text

            print(cnt, datetime, title, href)
            HACG_Processor.data.append((cnt, datetime, title, href))

        return "Request(callback=self.process_title)"

    def process_title(self, response):
        pass


if __name__ == "__main__":
    SpiderCore(HACG_Processor()).start()

    with open("output.txt", "w", encoding="utf-8") as file:
        print(*HACG_Processor.data, file=file, sep="\n")

    ls = list(filter(lambda x: x[0] != "回复", HACG_Processor.data))
    all = sorted(ls, key=lambda x: int(x[0].replace(",", "")), reverse=True)
    with open("output2.txt", "w", encoding="utf-8") as f:
        print(*all, file=f, sep="\n")
