---
date: 2022.11.19
title: 881. Boats to Save People
difficulty:
    - medium
runtime: 75.65 # faster than (in %)
memory usage: 31.04    # less than (in %)
---
## Description
You are given an array `people` where `people[i]` is the weight of the `ith` person, and an **infinite number of boats**where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

Return *the minimum number of boats to carry every given person*.

**Example 1:**

```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

```

**Example 2:**

```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

```

**Example 3:**

```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

```

**Constraints:**

- `1 <= people.length <= 5 * 104`
- `1 <= people[i] <= limit <= 3 * 104`

## Approach 1: Greedy with Two pointers
Time complexity: `O(nlog(n))`    |    Space complexity: `O(1)`
where `n` is the length of `people`

``` python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        n = len(people)
        
        i, j = 0, n-1
        
        ans = 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                
            j -= 1
            ans += 1
        
        return ans
```