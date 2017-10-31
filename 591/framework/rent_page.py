# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:10:02 2017

@author: housesu
"""
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import re

    
    
def start():
#prepare something like db
    
    pass

def end():
#end process 
    pass

def travel_pages(pageSource,start=None,end=None):

    if start !=None :
        start()
        
    while True:
        process_page()
        pass
    pass

    if end != None:
        end() 
#todo remove db parameter
def pager(pageSource,db,start=None,end=None):
    soup = BeautifulSoup(pageSource, 'lxml')  # 解析器接手
    content=soup.find('div',attrs={'id':'content'})
    col=['house_type','floor','address','price','area','viewer','connector','update_time','pic','link']
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
            new_db_line=[house_type, floors,address,price,area,viewer,connector,update_time,pic,link]
            
            '''
            print "house , floor, address, price ,pic ,area, link viewer"
            print new_db_line[0],new_db_line[1],new_db_line[2],new_db_line[3],new_db_line[4],new_db_line[5]
            print new_db_line[6],new_db_line[7],new_db_line[8],new_db_line[9]
            '''
            
            db_line = pd.DataFrame([new_db_line],columns=col)
            db.append(db_line)
            #print db
            #db.to_excel('debug.xlsx', sheet_name='Sheet1')
    print "total %d handled" % count
'''
#main
start()
travel_pages()
travel_lists()
#page_start
#page_process()
#page_end
end()

#main process
# element process
'''