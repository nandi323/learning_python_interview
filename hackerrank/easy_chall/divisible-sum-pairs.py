# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ar = sorted(ar)
    total = 0
    for idx,i in enumerate(ar):
        for jdx,j in enumerate(ar):
            if idx < jdx:
                if (i + j) % k == 0:
                    print(i, j)
                    total += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
