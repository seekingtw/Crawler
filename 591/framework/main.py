# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:23:41 2017

@author: housesu

main control 
"""

from selenium import webdriver
import time
import rent_page
from pandas import DataFrame

def start(browser):
    browser.get("https://rent.591.com.tw/?kind=0&region=3")
    time.sleep(3)

    #set localition.
    area=browser.find_element_by_css_selector('.pull-left[data-id="3"]')
    area.click()
    time.sleep(1)
    county=browser.find_element_by_xpath('//*[@id="optionBox"]/li[1]/label/span')
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
        time.sleep(5)
        elements = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
        if elements[0] == previous_check :
            break
        
        #times control
        times=times -1
        if times==0 :
            return 0
        
        page_count=page_count+1
        
    return 0
    pass

class Db :
    def __init__(self):
        self.pd= DataFrame()
        
    def append(self,dataframe):
        self.pd=self.pd.append(dataframe)        
        
    def to_excel(self, name,sheet_name='Sheet1'):
        self.pd.to_excel(name, sheet_name='Sheet1')

browser=webdriver.Firefox()
timestamp=time.strftime("%a-%b-%d-%H_%M_%S-%Y", time.localtime()) 
start(browser)
db =Db()

trace_pages(browser,rent_page.pager,db)
browser.quit()
db.to_excel(timestamp+'.xlsx')
