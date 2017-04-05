from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os
import traceback
import time

import utilities

class IkhwanWebCrawler(object):
    topic_url = "http://www.ikhwanweb.com/articles.php?pid=&start="
    domain_url = "http://www.ikhwanweb.com/"

    topic_url_filepath = os.path.expanduser('~') + "/Downloads/Data/IkhwanWeb/PostTopic_URL.txt"
    posts_filepath = os.path.expanduser('~') + "/Downloads/Data/IkhwanWeb/Post/Posts.tsv"

    total_page =  391# 3325 #add extract one than actual page numbers

    def __init__(self):
        self.client = webdriver.Firefox()
        # self.get_article_url(self.topic_url)
        self.extract_articles(self.topic_url_filepath)


    def get_article_url(self, url):
        for i in range(0,3901,10):
            page_url = url + str(i)
            print(page_url)
            self.extract_thread_url(page_url)


    def extract_thread_url(self, url):
        self.client.get(url)
        time.sleep(5)
        url_soup = bs(self.client.page_source)

        for single_article_url in url_soup.find_all("h2",{"class":"contentheading"}):
            head_news_url = single_article_url.find('a')['href']

            with open(self.topic_url_filepath, "a", encoding='utf-8') as text_file:
                text_file.write(head_news_url + "\n")

    def extract_articles(self, url):
        thread_url_link = utilities.read_text_file(url)

        for single_thread_url in thread_url_link:
            single_thread_url = single_thread_url.strip()
            article_url = self.domain_url + single_thread_url
            try:
                self.client.get(article_url)
                time.sleep(7)
                soup = bs(self.client.page_source, "html.parser")

                title = soup.title.string
                article_date = "abc"

                container = soup.find("div",{"id":"ja-container"})
                article = container.find("div",{"id":"vozme"})
                article = utilities.cleanText(article)

                article_info = [article_date,title,article]

                with open(self.posts_filepath, "a", encoding='utf-8') as text_file:
                    for item in article_info:
                        text_file.write("%s\t"  %item)
                    text_file.write("\n")
                print("-----------------")

            except Exception:
                traceback.print_exc()
        self.client.quit()

IkhwanWebCrawler()







