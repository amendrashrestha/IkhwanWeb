from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os
import traceback
import time

class IkhwanWebCrawler(object):
    topic_url = "http://www.ikhwanweb.com/article.php?id=32799"

    def __init__(self):
        self.client = webdriver.Firefox()
        self.extract_articles(self.topic_url)

    def extract_articles(self, url):
        try:
            self.client.get(url)
            time.sleep(10)
            soup = bs(self.client.page_source, "lxml")

            #testing
            title = soup.title.string

            container = soup.find("div",{"id":"ja-container"})
            article = container.find("div",{"id":"vozme"})

            print(title)
            print(article.text)

        except Exception:
            traceback.print_exc()
        self.client.quit()

IkhwanWebCrawler()







