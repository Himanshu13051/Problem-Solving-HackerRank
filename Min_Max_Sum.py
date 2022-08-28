#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    a = 0
    b = arr[0]
    sum = 0
    for i in arr:
        sum += i
        if i > a:
            a = i
    
        if i < b:
            b = i
    print(sum - a,sum - b)
    
    
    
    
            
        
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
