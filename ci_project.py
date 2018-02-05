# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""


class math:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def somme(self):
        s=float(self.x)+float(self.y)        
        return s
    
    @property 
    def soustraction(self):
        s=float(self.x)-float(self.y) 
        return s
    
    @property 
    def division(self):
        d=float(self.x)/float(self.y) 
        return d

    