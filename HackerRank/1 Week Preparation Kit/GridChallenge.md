# Grid Challenge

[Grid Challenge | HackerRank](https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four)

## Solution

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    n = len(grid)
    
    if n == 0:
        return 'YES'
    
    m = len(grid[0])
    
    new_grid = ['']*n
    
    for i in range(n):
        new_grid[i] = sorted(grid[i])
    
    print(new_grid)
    
    for i in range(n-1):
        for j in range(m):
            if new_grid[i][j] > new_grid[i+1][j]:
                return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
```

