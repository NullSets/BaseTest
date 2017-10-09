



from urllib import request
import re

p = re.compile("")
response = request.urlopen("")
for url,name in p.findall(response):
    print("%s (%s)" % (name,url))







