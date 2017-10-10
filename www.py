


from urllib import request

import re
p = re.compile("")
response = request.urlopen("")
for url,name in p.findall(response):
    print("%s (%s)" % (name,url))


# from urllib import request
# import re
#
# p = re.compile("")
# response = request.urlopen("")
# for url,name in p.findall(response):
#     print("%s (%s)" % (name,url))


from html.parser import HTMLParser

class Scraper(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
    def handle_startendtag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        pass
    def handle_charref(self, name):
        pass
    def handle_entityref(self, name):
        pass
    def handle_comment(self, data):
        pass
    def handle_decl(self, decl):
        pass
    def handle_pi(self, data):
        pass



"""
BeautifulSoup
"""
import bs4
from bs4 import BeautifulSoup
from urllib import request

# response = request.urlopen("http://python.org/community/jobs")
# text = response.read()
# soup = BeautifulSoup(text)

html_text = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_text,"lxml")
print(soup.prettify())
# Tags
print(soup.title) #<title>The Dormouse's story</title>
print(soup.head) #<head><title>The Dormouse's story</title></head>
print(soup.a) #<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print(soup.p) #<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# Tags 的两个属性: name,attrs
print(soup.name) #[document]
print(soup.head.name) #head
print(soup.p.attrs) #{'class': ['title'], 'name': 'dromouse'}
print(soup.p["class"]) #['title']
print(soup.p.get('class')) #['title']
print(soup.p.attrs['name'])
soup.p['class'] = 'newClass'
print(soup.p)
# NavigableString
print(soup.p.string)
print(type(soup.p.string))
# BeautifulSoup
print(type(soup.name))
print(soup.name)
print(soup.attrs)
# Comment
print(soup.a) #<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>    带注释的标签
print(soup.a.string)  #Elsie
print(type(soup.a.string)) #<class 'bs4.element.Comment'>
if type(soup.a.string) == bs4.element.Comment:
    print(soup.a.string)
if isinstance(soup.a.string,bs4.element.Comment):
    print("yes")









