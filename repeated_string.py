# https://www.hackerrank.com/challenges/repeated-string/problem
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    a_per_string = s.count("a")
    nr_of_strings_in_n = n // len(s)
    div_of_string = s[:(n % len(s))]
    a_in_div = div_of_string.count("a")

    total_a = a_per_string * nr_of_strings_in_n + a_in_div
    return total_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
