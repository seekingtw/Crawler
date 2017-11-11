# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:16:02 2017

@author: housesu
"""

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from pandas_db import *
#viewer','connector','pic'
import re


def process_item_page(db, page_source,link_adress,browser=None):
    soup=BeautifulSoup(page_source,'lxml',from_encoding='utf-8')
    #print(soup.prettify("utf-8"))
    #handle_page(handle_pics,handle_overview,handle_brief,handle_thing,soup,db,link_adress)
    handle_page(soup,db,link_adress,None,handle_overview,handle_brief,None,handle_gps,browser)
    
    pass
    
class Item:
    pass

def print_element(element,prefix="",postfix="",enable=False):
    if enable!=True:
        return
    print prefix
    print element.prettify("utf-8")
    print postfix
    pass

def print_elements(elements,enable=False):
    if enable!=True:
        return
    print "total elements %d " % len(elements)
    count = 0;
    for each in elements:
        print_element(each," =============elements ==========="+str(count), "",True)
        count=count+1


def handle_page(soup,db,link,pic_sub=None,overview_sub=None,brief_sub=None,thing_sub=None,gps_sub=None,browser=None):
   #global soup
    col=['house_type','room_type','price','area','floor','address','update_time','due','link' \
'gender', 'fee']
    item=Item()
    image_sections =soup.find_all('div',attrs={'class':'imgList'})
    print_elements(image_sections,False)

    '''
    # 2 section , only first is usable.
     for each in image_sections:
        print "======="
        print each.prettify("utf-8")
    '''
    if pic_sub!= None: pic_sub(image_sections[0],item)
    
    right_box=soup.find_all('div',attrs={'class':'rightBox'})
    if len(right_box)==0:
        print "link %s is not existed anymore "% link 
        return
    print_elements(right_box,False)
    if overview_sub!= None: overview_sub(right_box[0],item)
    
    brief_sections=soup.find_all('ul',attrs={'class':'clearfix labelList'})
    print_elements(brief_sections,False)
    if brief_sub != None: brief_sub(brief_sections[0],item)
    
    thing_sections=soup.find_all('ul',attrs={'class':'facility clearfix'})
    print_elements(thing_sections,False)
    if thing_sub != None : thing_sub(thing_sections[0],item)
    
    gps_sections=soup.find('div',attrs={'class':'contenter banner'})
    if gps_sub!= None : gps_sub(gps_sections,item,browser)     
    #address of google 
    #print soup.find_all('span',attrs={'class':'addr'})
    string_temp = str(soup.find_all('span',attrs={'class':'addr'}))
    string_temp=  unicode(string_temp,'unicode-escape');#####special
    #print string_temp
    item.address=string_temp
    item.address= item.address.replace('[<span class="addr">','')
    item.address= item.address.replace('</span>]','')
    #print item.__dict__

    new_item=pd.DataFrame(\
    [[item.house_type, item.room_type, item.price, item.area,item.floor,
    item.address,item.update_time, item.due,link, item.gender,item.fee,item.phone,item.gps_link]],   \
    columns=['house_type','room_type','price','area','floor',
    'address','update_time','due','link' ,'gender', 'fee','phone','gps_link'])
    print new_item
    db=db.append(new_item)
    

def handle_thing(section,item):
    print_element( section,"","",False)
    lis=section.find_all('li')
    print_elements(lis,False)
    for each in lis:
        key=each.text
        have=each.span.attrs['class'][0]
        print type( have)
        
        if have != "no":
            have="yes"
        print "result : %s %s " %(key,have)
    pass

def handle_address():
    pass

def handle_pics(section,item):
        #image_section=soup.find("div",attrs={'class':'imgBox'})
    print_element(section,"=="*3,"",False)
    ols=section.find_all('ol')
    print_elements(ols,False)
    #only 1 ol 
    imgs=ols[0].find_all('img')
    print_elements(imgs,False)
    for each in imgs:
        address=each.attrs['lazysrc']
        title=each.attrs['title'];
        print address, title
    
    pass
def handle_gps(gps_sections,item,browser=None):
    gps_string=gps_sections.find('textarea',attrs={'class':'datalazyload'}).text
    re_result=re.search('src="(.*?)"',gps_string)
    gps_link=re_result.group(1)
    gps_link="https://rent.591.com.tw/"+gps_link
    
    item.gps_link=gps_link

    if browser!= None:
        browser.get(gps_link)
        time.sleep(1)
        #element = browser.find_element_by_xpath('//*[@id="mapDiv"]/div/div/div[9]/div/div/div/div[1]/div')
        soup2 = BeautifulSoup(browser.page_source, 'lxml')  # 解析器接手
        bar=soup2.find('div',attrs={'class':'propMapBarMap'})
        #print bar.iframe.attrs['src']
        gps_string= bar.iframe.attrs['src']
        re_result=re.search('&q=(.+?)&',gps_string);
        if re_result!=None:
            gps_locate= re_result.group(1)
            item.gps_link=gps_locate
        #print soup
    print item.gps_link
def kv_dic(string,dict_item,splitor,keys ):
    '''
    (v1,v2)=string.split(":")
    v1=v1.strip()
    v2=v2.strip()
    dict_item[v1]=v2
    if u'坪數' in lis_dic: area=lis_dic[u'坪數']
    if u'現況' in lis_dic: room_type=lis_dic[u'現況']
    if u'型態' in lis_dic: house_type=lis_dic[u'型態']
    if u'樓層' in lis_dic: floor=lis_dic[u'樓層']
    if u'社區' in lis_dic: community=lis_dic[u'社區'] 
    '''
    pass

def handle_overview(section,item):
    lis=section.find_all('li')
    print_elements(lis,False)
    lis_dic={}
    (area,floor,house_type,room_type,community)=('','','','','')
    for each in lis:
        (v1,v2)=each.text.split(":")
        v1=v1.strip()
        v2=v2.strip()
        lis_dic[v1]=v2
    if u'坪數' in lis_dic: area=lis_dic[u'坪數']
    if u'現況' in lis_dic: room_type=lis_dic[u'現況']
    if u'型態' in lis_dic: house_type=lis_dic[u'型態']
    if u'樓層' in lis_dic: floor=lis_dic[u'樓層']
    if u'社區' in lis_dic: community=lis_dic[u'社區']
    
    price= section.find('div',attrs={'class', 'price clearfix'}).text
    price=price.strip()
    price=re.sub(u'[(元/月)(\n)]','',price);
    print area,floor,house_type,room_type,community,price
     
    phone=0 ##TODO : OCR to get data
    #parser update and avail date.
    (due,update)=("","")
    date_spans = section.find('div', attrs={'class','explain clearfix'}).find_all('span')
    date_dic={}    
    for each in date_spans:
        temp_list=each.text.split(u'：')
        print temp_list
        for idx in range(len(temp_list)):temp_list[idx].strip()
        if len(temp_list) ==2 : date_dic[temp_list[0]]=temp_list[1]
    if u'更新於' in date_dic: update=date_dic[u'更新於']
    if u'有效期' in date_dic: due=date_dic[u'有效期']
    
    user_info = section.find('div', attrs={'class','userInfo'}).find_all('span')    
    #time_phone=section.find_all('span')
    #print_elements(time_phone,False)
    mobile=""
    #mobile=time_phone[2].text
    #num= time_phone[3].text
    num=""
    
    print update,due,mobile,num
    item.update_time=update
    item.due=due
    item.area=area
    item.floor=floor
    item.house_type=house_type
    item.room_type=room_type
    item.price=price
    item.community=community
    #item.mobile=mobile
    item.phone=num;
    #update=explain clearfix
    #due=
        
    pass

def handle_brief(section,item):
    print_element(section,"","",enable=False)
    lis=section.find_all('li')
    print_elements(lis,False)
    brief_dic={}
    for each in lis:
        #print each.text
        ds= each.text.split(u'：')
        print "%s : %s" % (ds[0],ds[1])
        brief_dic[ds[0]]=ds[1]
    #print brief_dic
    item.fee=0
    item.gender=""
    if u'性別要求' in brief_dic: item.gender=brief_dic[u'性別要求']
    if u'管理費' in brief_dic: item.fee=brief_dic[u'管理費']
    pass

def trace_test(browser,test_pages,times=-1):
    db_item=Db("item_test_")
    for each_link in test_pages:
        #print each
        times-=1
        browser.get(each_link)
        time.sleep(2)
        process_item_page(db_item,browser.page_source,each_link,browser)
        if times ==0 : break
    db_item.to_excel()
    pass


if __name__ == "__main__":
    browser=webdriver.Chrome()
    #browser.get("https://rent.591.com.tw/?kind=0&region=3")
    test_pages=['https://rent.591.com.tw/rent-detail-5774424.html']
    trace_test(browser,test_pages)
