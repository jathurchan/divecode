# Min-Max Sum

[Mini-Max Sum | HackerRank](https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one)

## Solution

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    n = len(arr)
    
    minTotal, maxTotal = float('inf'), 0
    
    for i in range(n):
        total = 0
        for j in range(n):
            if i != j:
                total += arr[j]
        if total >= maxTotal:
            maxTotal = total
        if total <= minTotal:
            minTotal = total
        
    print(f"{minTotal} {maxTotal}")
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
```

