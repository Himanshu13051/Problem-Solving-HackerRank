#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    small = b[0]
    # for i in range(0, len(b)):
    #    if b[i] < small:
    #     small = b[i]
       
    number = 0
    
    
    for i in range(1, small+1):
        x = False
        for j in a:
            if i % j == 0:
                x = True
            else:
                x = False
                break
        if x == True:
            y = False
            for k in b:
                if k % i == 0:
                    y = True
                else:
                    y = False
                    break
            if y == True:
                number += 1
    return number
                
        

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
