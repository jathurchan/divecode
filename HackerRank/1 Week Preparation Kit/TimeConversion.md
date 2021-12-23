# Time Conversion

[Time Conversion | HackerRank](https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one)

## Solution

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s.split(':')
    if time[-1][2:] == 'AM':
        if time[0] == '12':
            return (f'00:{time[1]}:{time[2][:2]}')
        else:
            return (f'{time[0]}:{time[1]}:{time[2][:2]}')
    else:
        if time[0] == '12':
            return (f'12:{time[1]}:{time[2][:2]}')
        else:
            return (f'{int(time[0])+12}:{time[1]}:{time[2][:2]}')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
```

