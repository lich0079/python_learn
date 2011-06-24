# coding:utf-8'
'''
Created on 2011-4-20

@author: lich0079
'''
a=['1']
for i in range(30):
    elem=a[-1]+'?' #a最新的元素
    next=[]
    start=0
    for end in range(len(elem)):
        if elem[end]!=elem[start]:# 遍历找到一个前后数字不一样的
            next.append(str(end-start)+elem[start]) #记下几个几
            start=end
    a.append(''.join(next))
print len(a[-1])