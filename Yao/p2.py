#!/usr/bin/env python
# encoding: utf-8

from HTMLParser import HTMLParser
import urllib2, string

req = urllib2.Request('http://www.pythonchallenge.com/pc/def/ocr.html')
response = urllib2.urlopen(req)
html = response.read()

class MyHTMLParser(HTMLParser):
    times= 0
    def handle_comment(self, data):
        self.times += 1
        if self.times == 2:
            print filter(lambda x:x in string.letters, data)

parser = MyHTMLParser()
parser.feed(html)
