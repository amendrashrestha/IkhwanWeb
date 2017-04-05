__author__ = 'amendrashrestha'

import re


def cleanText(post):
    post = post.text
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    post = tag_re.sub('', post)
    post = post.replace("\n"," ").strip()
    post = post.replace("\r"," ").strip()
    post = post.replace("\t"," ").strip()
    return post

def read_text_file(filepath):
    with open(filepath) as content:
        topic_url = content.readlines()
        return topic_url

def write_text(text, filepath):
    with open(filepath, "a") as content:
        content.write(text)
        content.write("\n")
