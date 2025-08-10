#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    max_color = max(ar) 
    counts = [0] * (max_color + 1) 
    for color in ar:
        counts[color] += 1

    
    pairs = 0
    for count in counts:
        pairs += count // 2 

    return pairs


# Example usage
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))  # Output: 3

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
