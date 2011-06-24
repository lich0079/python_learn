# -*- coding: utf-8 -*- 

import urllib  
import re
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num="12345"
text = urllib.urlopen(url+num).read()
count =1
m = re.findall("(\d*)$",text)
while m[0] :
    num = m[0]
    text = urllib.urlopen(url+num).read()
    count +=1
    print num +"  "+ text+  "   "+ str(count)
    m = re.findall("(\d*)$",text)
print "============="+num
num = str(int(num)/2)
print "yyyyyyyyyyyyy"+num
text = urllib.urlopen(url+num).read()
count +=1
print num +"  "+ text+  "   "+ str(count)
m = re.findall("(\d*)$",text)

while m[0] :
    num = m[0]
    text = urllib.urlopen(url+num).read()
    count +=1
    print num +"  "+ text+  "   "+ str(count)
    m = re.findall("(\d*)$",text)
num = str(int(num)/2)
text = urllib.urlopen(url+num).read()
count +=1
print num +"  "+ text+  "   "+ str(count)
m = re.findall("(\d*)$",text)

while m[0] :
    num = m[0]
    text = urllib.urlopen(url+num).read()
    count +=1
    print num +"  "+ text+  "   "+ str(count)
    m = re.findall("(\d*)$",text)
