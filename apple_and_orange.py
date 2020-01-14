# https://www.hackerrank.com/challenges/apple-and-orange/problem


import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    nr_app = 0
    nr_or = 0
    for item in apples:
        item = item + a
        if t >= item >= s:
            nr_app += 1
    for item in oranges:
        item = item + b
        if t >= item >= s:
            nr_or += 1
    print(nr_app)
    print(nr_or)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
