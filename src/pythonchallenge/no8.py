# coding:utf-8'
import base64
import bz2
import urllib2
'''
Created on 2011-4-20

@author: lich0079
'''
url = 'http://www.pythonchallenge.com/pc/return/good.html'
un = bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
pw = bz2.decompress('BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')


b64str = base64.encodestring('%s:%s' % (un, pw))

req = urllib2.Request(url)
auth = 'Basic %s' % b64str
req.add_header('Authorization', auth)
try:
    opener = urllib2.urlopen(req)
    print opener.read()
except IOError, e:
    print str(e)



