from selenium import webdriver
import time


#help(webdriver)
browser=webdriver.Chrome()
browser.get("https://rent.591.com.tw/?kind=0&region=3")
#main content
#element = browser.find_element_by_id("content")
#print element.get_attribute("innerHTML")
time.sleep(10)
#first page
element = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
#print element.get_attribute("innerHTML")
#print (element)
for each in element:
    print each.get_attribute("innerHTML")
time.sleep(5)

#next
elements = browser.find_elements_by_css_selector("a.pageNext")
print len(elements)
type(elements)
element=elements[0]
print element
element.click()

#second page
element = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
#print element.get_attribute("innerHTML")
#print (element)
for each in element:
    print each.get_attribute("innerHTML")
