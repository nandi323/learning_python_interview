# https://www.hackerrank.com/challenges/2d-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    length = len(arr)-1
    maxim = None

    for i in range(length-1):
        print(i)
        for j in range(length-1):
            if maxim == None or maxim < add_hourglass(arr, i,j):
                maxim = add_hourglass(arr, i,j)
    return(maxim)

def add_hourglass(array, i, j):
    hour_sum_top = array[i][j] + arr[i][j + 1] + arr[i][j+2]
    hour_sum_mid =              array[i+1][j+1]
    hour_sum_bottom = array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
    return hour_sum_top + hour_sum_mid + hour_sum_bottom

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
