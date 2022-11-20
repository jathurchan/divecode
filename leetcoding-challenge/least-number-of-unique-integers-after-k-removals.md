---
date: 2022.11.19
title: 1481. Least Number of Unique Integers after K Removals
difficulty:
    - medium
runtime: 39.86 # faster than (in %)
memory usage: 77.77    # less than (in %)
---
## Description
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

## Approach 1: Greedy
Time complexity: `O(nlog(n))`    |    Space complexity: `O(n)`
where `n` is the length of `arr`

``` python
from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:        
        
        counts = defaultdict(int)
        
        for num in arr:
            counts[num] += 1
        
        freq = sorted(counts.values(), reverse=True)
        
        while k:
            val = freq[-1]
            if val <= k:
                k -= val
                freq.pop()
            else:
                break
        
        return len(freq)
```