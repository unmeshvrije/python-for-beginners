#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 12:22:32 2019

@author: unmesh
"""

def logger(fun_ref):
    def fun_wrapper():
        print ("Entering the function ", fun_ref.__name__)
        result = fun_ref()
        print ("Exiting the function ", fun_ref.__name__)
        return result
    return fun_wrapper

@logger
def fun():
    print("fun")

@logger
def gun():
    fun()
    print("gun")
    
@logger
def hun():
    print("hun")
    
    
def mess():
    fun()
    gun()
    hun()
    gun()
    
    
#gun()
hun()
#mess()