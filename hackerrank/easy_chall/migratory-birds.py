# https://www.hackerrank.com/challenges/migratory-birds/problem

import math
import os
import random
import re
import sys

from collections import Counter


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    b = set(arr)
    b_count = [arr.count(x) for x in b]
    b_max = max(b_count)
    selected = max(arr)

    for i,j in zip(b,b_count):
        if j == b_max:
            if i < selected:
                selected = i
    return(selected)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()