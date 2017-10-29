# -*- coding: utf-8 -*-

from selenium import webdriver
import time

#get first page
browser=webdriver.Firefox()
browser.get("https://rent.591.com.tw/?kind=0&region=3")
time.sleep(3)

#set localition.
area=browser.find_element_by_css_selector('.pull-left[data-id="3"]')
area.click()
time.sleep(1)
orz2=browser.find_element_by_xpath('//*[@id="optionBox"]/li[1]/label/span')
orz2.click()
time.sleep(1)

#get data
print "get information start: " 
page_count=1;
while True:
    elements = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
    previous_check=elements[0]
    print "page %d\n" %(page_count)
    for each in elements:
        print each.get_attribute("innerHTML")
    next_page = browser.find_element_by_css_selector("a.pageNext")
    next_page.click();
    time.sleep(2)
    elements = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
    if elements[0] == previous_check :
        break
    page_count=page_count+1
print "get information done: " 
browser.quit()
