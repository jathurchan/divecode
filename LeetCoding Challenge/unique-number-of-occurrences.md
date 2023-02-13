---
date: 2022.11.30
title: 1207. Unique Number of Occurrences
difficulty:
    - easy
runtime: 99.95 # faster than (in %)
memory usage: 72.74    # less than (in %)
---
## Description
Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique**, or `false` otherwise.

**Example 1:**

```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

**Example 2:**

```
Input: arr = [1,2]
Output: false

```

**Example 3:**

```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

```

**Constraints:**

- `1 <= arr.length <= 1000`
- `1000 <= arr[i] <= 1000`

## Approach 1: hashmap
Time complexity: `O(n + plog(p))`    |    Space complexity: `O(p)`
where `n` is the length of `arr` and `p <= 1000` the number of unique numbers

``` python
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        
        for val in arr:
            counts[val] += 1
        
        values = sorted(counts.values())
        
        for i in range(len(values)-1):
            if values[i+1] == values[i]:
                return False
        
        return True
```