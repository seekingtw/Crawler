# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:27:09 2017

@author: housesu
"""

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import re
from bs4 import BeautifulSoup

soup=BeautifulSoup(open('591.html'),'lxml',from_encoding='utf-8')
print(soup.prettify("utf-8"))

content=soup.find('div',attrs={'id':'content'})

#print content.prettify("utf-8")
print len(content)
count =0
for each in content:
    if each.title == None:
        print "--------count %d--------"  %count
        if each.em == None :
            continue
        print each.em.text
        print each.find('div',attrs={'class':'price'}).i.text
        print each.a
        print each.a.attrs['href']
        print each.img
        a =each.find_all('p',attrs={'class':'lightBox'})
        print len(a)
        for each in a:
            data=each.text
            data=re.sub(r'\s','',data)
            data=re.sub(r'\xa0','',data)
            data=re.sub(r'\u3000','',data)
            infos= data.split('|')
            #match = re.search(r'\d坪', data) 
            #if match!= None:
            print infos
        #image_src= each.img.attrs['src'].replace(u'【新北市出租】-591房屋交易網_files',"591_files")
        #print image_src
        #image_inst= mpimg.imread(image_src)
        #plt.imshow(image_inst) # 显示图片
        #plt.show()
        #em=each.find_all("em")
        #print em[0]
        #print em[1]
        '''
        i=0
        for each2 in each.find_all("em"):
            print "%d ,%s" %(i,each2.text)
            i=i+1
        print "---------------------"
        '''
        count=count+1
print count