#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:20:57 2019

@author: unmesh
"""

import random
import sys

def generate_random_number():
    while True:
        yield random.random() * 75    

# The code to accept the input from user
# n = int(input("How many random numbers do you want : "))

# The code to read the input from command line option
# prints the argument vector
print(sys.argv)

# access the command line argument at index 1
# convert it into an integer
n = int(sys.argv[1])

print("<3"*50)
# assign a generator object to rand
rand = generate_random_number()
start = 0

# If you keep the same seed, you will get the same
# set of random numbers
random.seed(41)
while start < n:
    print(next(rand))
    start += 1
