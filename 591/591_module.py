# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from bs4 import BeautifulSoup

#%pylab inline
import matplotlib.pyplot as plt # plt 用于显示图片
import pandas as pd
from pandas import DataFrame
import re
"""
Created on Mon Oct 30 23:55:34 2017

@author: housesu
"""
#global

db =DataFrame()
browser=None
#inital

def start():
    global browser
    browser=webdriver.Firefox()
    browser.get("https://rent.591.com.tw/?kind=0&region=3")
    time.sleep(3)

    #set localition.
    area=browser.find_element_by_css_selector('.pull-left[data-id="3"]')
    area.click()
    time.sleep(1)
    county=browser.find_element_by_xpath('//*[@id="optionBox"]/li[1]/label/span')
    county.click()
    time.sleep(1)

def done():
    global browser
    browser.quit()
    
def exe_page( page_function):
    global browser
    page_count=1;
    while True:
        print "page %d" % page_count
        ##the way to check end is dirty ...refine it.
        elements = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
        previous_check=elements[0]
        
        page_function()
        
        next_page = browser.find_element_by_css_selector("a.pageNext")
        next_page.click();
        time.sleep(5)
        elements = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
        if elements[0] == previous_check :
            break
        page_count=page_count+1
        #print "get information done: " 
        

def process_page():
    global browser
    global db
    
    pageSource = browser.page_source  # 取得網頁原始碼
    soup = BeautifulSoup(pageSource, 'lxml')  # 解析器接手

    content=soup.find('div',attrs={'id':'content'})
    col=['house_type','floor','address','price','pic','area','link','viewer','connector','update_time']
    print len(content)
    count =0
    for each in content:
        if each.title != None:
            continue
        print "--------count %d--------"  %count
        #print each
        count=count+1
        
        if each == None or each.em == None :
            continue
        
        ems=each.find_all('em')
        address= ems[0].text
        connector=ems[1].text
        update_time=ems[2].text
        update_time=re.sub(u'內更新','',update_time)
        if len(ems) == 4:
            viewer=ems[3].text
        elif len(ems)==5:
            viewer=ems[4].text
        elif len(ems) == 3:
            viewer="0"
        else:
            print "unexpect => %d" % (len(ems))
            for ems_each in ems:
                print ems_each
            print ""
        viewer=re.sub(u'瀏覽','',viewer)
        price=each.find('div',attrs={'class':'price'}).i.text
        link= each.a.attrs['href']
        link=re.sub(u'//','https://',link);
        pic=image_src= each.img.attrs['src']
        
        ## handle floor/area/type
        physical_info =each.find_all('p',attrs={'class':'lightBox'})
        #print len(a)
        for each in physical_info:
            data=each.text
            if data.find('|') == -1: 
                #print "spe: %s " % data
                continue
            data=re.sub(r'\s','',data)
            data=re.sub(r'\xa0','',data)
            data=re.sub(r'\u3000','',data)
            datas = (data.split('|'))
            
            house_type=datas[0]
            #print house_type
            if len(datas) == 3:
                area=datas[1]
                floors=datas[2]
            elif len(datas) == 4:
                area=datas[2]
                floors=datas[3]                
            else:
                print "%d ==> %s" %(len(datas), data)
            
            area=re.sub(u'坪','',area)
            floors=re.sub(u'樓層：','',floors)
           
            #print "[[%s %s %s]]" %(house_type, area,floors)
            new_db_line=[house_type, floors,address,price,pic,area,link,viewer,connector,update_time]
            
            '''
            print "house , floor, address, price ,pic ,area, link viewer"
            print new_db_line[0],new_db_line[1],new_db_line[2],new_db_line[3],new_db_line[4],new_db_line[5]
            print new_db_line[6],new_db_line[7],new_db_line[8],new_db_line[9]
            '''
            
            db_line = pd.DataFrame([new_db_line],columns=col)
            db=db.append(db_line)
    print "total %d handled" % count
    #print db
    
start()
exe_page(process_page)
print db
done()
db.to_excel('591.xlsx', sheet_name='Sheet1')
