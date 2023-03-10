---
date: 2022.11.15
title: 2248. Intersection of Multiple Arrays
difficulty:
    - easy
runtime: 99.72 # faster than (in %)
memory usage: 93.11    # less than (in %)
---
## Description
Given a 2D integer array `nums` where `nums[i]` is a non-empty array of **distinct** positive integers, return *the list of integers that are present in **each array** of* `nums` *sorted in **ascending order***.

**Example 1:**

**Input:** nums = [[**3**,1,2,**4**,5],[1,2,**3**,**4**],[**3**,**4**,5,6]]

**Output:** [3,4]

**Explanation:**

The only integers present in each of nums[0] = [**3**,1,2,**4**,5], nums[1] = [1,2,**3**,**4**], and nums[2] = [**3**,**4**,5,6] are 3 and 4, so we return [3,4].

**Example 2:**

**Input:** nums = [[1,2,3],[4,5,6]]

**Output:** []

**Explanation:**

There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

**Constraints:**


- `1 <= nums.length <= 1000`
- `1 <= sum(nums[i].length) <= 1000`
- `1 <= nums[i][j] <= 1000`
- All the values of `nums[i]` are **unique**.


## Approach 1: Hashmap
Time complexity: `O(m*(n+log(m)))`    |    Space complexity: `O(n*m)`
where `n` is the length of `nums` and `m` is the average of `nums[i]`


``` python
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        
        for row in nums:
            for num in row:
                counts[num] += 1
        
        
        res = []
        
        for key, freq in counts.items():
            if freq == len(nums):
                res.append(key)
        
        return sorted(res)
```