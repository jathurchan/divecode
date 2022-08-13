# Plus Minus

[Plus Minus | HackerRank](https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one)

## Solution

```python
#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    l = len(arr)
    
    p, n, z = 0., 0., 0.
    
    for num in arr:
        if num > 0:
            p += 1
        elif num < 0:
            n += 1
        else:
            z += 1
    
    print("{0:.6f}".format(p/l))
    print("{0:.6f}".format(n/l))
    print("{0:.6f}".format(z/l))
            

if __name__ == '__main__':
    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
```

