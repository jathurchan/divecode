# Caesar Cipher

[Caesar Cipher | HackerRank](https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three)

## Solution

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    result = ""
    for c in s:
        if (c >= 'A' and c <= 'Z'):
            result += chr(((ord(c) - ord('A') + k) % 26) + ord('A'))
        elif (c >= 'a' and c <= 'z'):
            result += chr(((ord(c) - ord('a') + k) % 26) + ord('a'))
        else:
            result += c
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
```

