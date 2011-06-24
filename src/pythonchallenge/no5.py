import cPickle
import urllib
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = cPickle.load(urllib.urlopen(url))
for i in data:
    for j in i:
        print j[0]*j[1],
    print


