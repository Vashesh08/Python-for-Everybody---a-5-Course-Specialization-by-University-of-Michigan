import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

user_input = input()

if re.search(pattern, user_input):
    print("Valid email")
else:
    print("Invalid Email")


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    i = d
    # while i>0:
    #     j = len(a)-1
    #     temp = a[j]
    #     j-=1
    #     while j>=0:
    #         temp2 = a[j]
    #         a[j] = temp
    #         temp = temp2
    #         j-=1
    #     a[-1] = temp
    #     i-=1
    t = []
    k = len(a)
    temp = d
    t.append(a[d])
    d += 1
    if d >= k:
        d -= k
    for i in range(k):
        if temp == d:
            break
        t.append(a[d])
        d += 1
        if d >= k:
            d -= k
    return t
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
