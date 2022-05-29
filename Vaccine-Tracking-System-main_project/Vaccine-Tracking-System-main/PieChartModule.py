# -*- coding: utf-8 -*-
"""
Created on Thur May 19 01:57:31 2022

@author: Mostafa Hassan
"""
import matplotlib.pyplot as plt

def piechart(n1,n2,L1,L2,name):

    def func(pct):
      return "{:1.1f}%".format(pct)
     
    plt.pie([n1,n2], labels=[L1,L2], autopct=lambda pct: func(pct)) 
    plt.title(name)
    plt.axis('equal')
    plt.show()
