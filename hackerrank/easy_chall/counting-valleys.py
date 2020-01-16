# https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    a = []
    sum = 0
    valley_counter = 0
    for char in s:
        if char == "U":
            a.append(1)
        else:
            a.append(-1)
    for num in a:
        if sum == 0:
            WE_RISK_VALLEY = True
        sum = sum + num
        if WE_RISK_VALLEY and sum < 0:
            WE_RISK_VALLEY = False
            valley_counter += 1
    return valley_counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
