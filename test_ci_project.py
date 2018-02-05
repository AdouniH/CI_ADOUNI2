# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

from ci_project import math
import unittest

class test_ci_projet(unittest.TestCase):
    def test_somme(self):
        m1=math(1,2)
        m2=math(-8,9)
        self.assertEqual(m1.somme,3)
        self.assertEqual(m2.somme,1)
        
    def test_soustraction(self):
        m1=math(4,2)
        m2=math(18,9)
        self.assertEqual(m1.soustraction,2)
        self.assertEqual(m2.soustraction,9)
        
    def test_division(self):
        m1=math(1,2)
        m2=math(-8,8)
        self.assertEqual(m1.division,0.5)
        self.assertEqual(m2.division,-1)
    
if __name__ =="__main__":
    unittest.main()