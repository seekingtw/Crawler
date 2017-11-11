# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:23:41 2017

@author: housesu

main control 
"""

from selenium import webdriver
import time
import rent_page
import item_page
from pandas_db import *
from pandas import DataFrame

def start(browser):
    browser.get("https://rent.591.com.tw/?kind=0&region=3")
    time.sleep(3)

    #set localition.
    area=browser.find_element_by_css_selector('.pull-left[data-id="3"]')
    area.click()
    time.sleep(1)
    #county=browser.find_element_by_xpath('//*[@id="optionBox"]/li[1]/label/span')#banqiao
    #county=browser.find_element_by_xpath('//*[@id="optionBox"]/li[9]/label/span')#tucheng
    county=browser.find_element_by_xpath('//*[@id="optionBox"]/li[4]/label/span')#xinzhong
    county.click()
    time.sleep(1)

def end(brower):
    pass

def trace_pages(browser,pager,db, times=-1) :
    if browser == None:
        return 0
    page_count=1;
    while True:
        print "page %d" % page_count
        ##the way to check end is dirty ...refine it.
        elements = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
        previous_check=elements[0]
        
        pager(browser.page_source,db )
        
        next_page = browser.find_element_by_css_selector("a.pageNext")
        next_page.click();
        time.sleep(7)
        elements = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
        if elements[0] == previous_check :
            break
        
        #times control
        times=times -1
        if times==0 :
            return 0
        
        page_count=page_count+1
    print "done %d pages" % page_count
    return 0
    pass

def trace_items(browser,db,times=-1):
    #db_item=Db("tucheng-item")
    db_item=Db("xinzhong-item")
    item_len=len(db.pd)
    count=0
    for each_link in db.pd['link']:
        print "%d in %d " % (count ,item_len)
        count+=1
        #print each
        times-=1
        browser.get(each_link)
        time.sleep(2)
        item_page.process_item_page(db_item,browser.page_source,each_link,browser=browser)
        if times ==0 : break
    db_item.to_excel()
    pass


if __name__ == "__main__":
    #browser=webdriver.Firefox()
    browser=webdriver.Chrome()
    
    start(browser)
    #db =Db("tucheng-list")
    db =Db('xinzhong-list')
    #db_item=Db()
    
    trace_pages(browser,rent_page.pager,db)
    
    trace_items(browser,db)
    #wait=input("type to continue")
    browser.quit()
    db.to_excel()
    #db_item.to_excel(timestamp+'_item.xlsx')

