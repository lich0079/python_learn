# coding:utf-8
import Image
import urllib

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
imgPath='./tmp/oxygen.png'
urllib.urlretrieve(url,imgPath)
im = Image.open(imgPath)
print "Image info:",im.format, im.size, im.mode
y_begin = 0
while True:
    p = im.getpixel((0, y_begin))
    print p
    if p[0] == p[1] == p[2]:
        break
    y_begin += 1
