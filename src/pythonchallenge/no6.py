# coding:utf-8
'''
Created on 2011-4-20

@author: lich0079
'''
import os
import re
import urllib
import zipfile
zipName = 'channel.zip'
os.remove(zipName)
url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
urllib.urlretrieve(url, zipName)
zf = zipfile.ZipFile(zipName)
extractPath='./tmp'
zf.extractall(extractPath)

f  = open(extractPath+'/90052.txt')
line  = f.readline()
m = re.findall("(\d*)$",line)
while m[0] :
    num = m[0]
    print zf.getinfo(num+'.txt').comment,
    f.close()
    f  = open(extractPath+'/'+num+'.txt')
    line  = f.readline()
    m = re.findall("(\d*)$",line)
#oxygen