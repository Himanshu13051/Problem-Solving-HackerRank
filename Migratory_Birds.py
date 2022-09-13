#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    temp = {}
    maxc = 0
    maxv = 0
    for i in range(len(arr)):
        if arr[i] in temp.keys():
            temp[arr[i]] += 1
            if temp[arr[i]] > maxc:
                maxc = temp[arr[i]]
                maxv = arr[i]
                
            if temp[arr[i]] == maxc:
                if maxv > arr[i]:
                    maxv = arr[i]
            
        else:
            temp[arr[i]] = 1
    return maxv        
        
            
      
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
  
