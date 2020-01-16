# https://www.hackerrank.com/challenges/jumping-on-the-clouds

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    for idx,item in enumerate(c):
        if item != 1:
            if idx + 2 == len(c) -1 or idx + 1 == len(c)-1:
                jumps += 1
                return jumps
            if c[idx + 2] == 0:
                jumps += 1
                c[idx +1] = 1
            elif c[idx + 1] == 0:
                jumps += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
