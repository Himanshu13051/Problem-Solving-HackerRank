import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(n):
        s = ""
        for j in range(n):
            if j >= n-1-i:
                s += "#"
            else:
                s += " "
        print(s)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
