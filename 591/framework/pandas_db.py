# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 00:47:46 2017

@author: housesu
"""
import time
import pandas as pd
class Db :
    def __init__(self,name):
        self.time=time.strftime("%a-%b-%d-%H_%M_%S-%Y", time.localtime()) 
        self.pd= pd.DataFrame()
        self.name=name
        
    def append(self,dataframe):
        self.pd=self.pd.append(dataframe)        
        
    def to_excel(self, prefix="",sheet_name='Sheet1'):
        self.pd.to_excel(prefix+self.name+self.time+".xlsx", sheet_name='Sheet1')