

from urllib import request

import re
p = re.compile("")
response = request.urlopen("")
for url,name in p.findall(response):
    print("%s (%s)" % (name,url))



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



