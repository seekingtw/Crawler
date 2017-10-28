from selenium import webdriver
import time


#help(webdriver)
browser=webdriver.Firefox()
browser.get("https://rent.591.com.tw/?kind=0&region=3")
### area 
#browser.implicitly_wait(10)
time.sleep(3)
#area=browser.find_element_by_css_selector('#area-select-box.area-box .clearfix .pull-left[data-id="6"]')
area=browser.find_element_by_css_selector('.pull-left[data-id="3"]')
area.click()
time.sleep(1)
#area_small
#area=browser.find_element_by_css_selector('li.clearfix.rion[data-bind="26"]')
#area.click()
print "3333"
orz1=browser.find_element_by_css_selector('span.search-location-span.select')
orz1.click()
time.sleep(1)
orz2=browser.find_element_by_xpath('//*[@id="optionBox"]/li[1]/label/span')
print orz2
orz2.click()
time.sleep(1)
print "333t"
#for each in orz1:
#    print each.text()

#browser.find_element_by_id("checktips26").click()
#browser.find_element_by_css_selector('#checktips26[data-bind="26"]').click()
time.sleep(3)
#main content
#element = browser.find_element_by_id("content")
#print element.get_attribute("innerHTML")
time.sleep(10)
#first page
element = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
#print element.get_attribute("innerHTML")
print (element)
print "first\n"
print len(element)
type(element)
browser.implicitly_wait(5)
for each in element:
    print each.get_attribute("innerHTML")
#time.sleep(5)

browser.implicitly_wait(5)
#next

elements = browser.find_elements_by_css_selector("a.pageNext")
print len(elements)
type(elements)
element=elements[0]
print element
element.click()
time.sleep(2)
#browser.implicitly_wait(5)
#browser.refresh()
#second page
element=""
element2 = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")

#browser.implicitly_wait(30)
time.sleep(2)
datas = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")

print (datas)
print "first\n"
print len(datas)
type(datas)
#print element.get_attribute("innerHTML")
#print (element)
for each in datas:
    print each.get_attribute("innerHTML")
'''
#browser.quit()
'''
next_page = browser.find_element_by_css_selector("a.pageNext")
previous_page=None
page_count=2
while(next_page!= None and previous_page!=datas[0]):
    previous_page=datas[0]
    next_page.click();
    time.sleep(3);
    datas = browser.find_elements_by_css_selector("ul.listInfo.clearfix p.lightBox em")
    if(previous_page==datas[0]):
        break
    print "page %d" % (page_count )
    page_count=page_count+1
    for each in datas:
        print each.get_attribute("innerHTML")
    next_page = browser.find_element_by_css_selector("a.pageNext")
        
browser.quit()
    