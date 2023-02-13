---
date: 2022.11.19
title: 875. Koko Eating Bananas
difficulty:
    - medium
runtime: 13.93 # faster than (in %)
memory usage: 24.98    # less than (in %)
---
## Description
Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k`bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

**Example 1:**

```
Input: piles = [3,6,7,11], h = 8
Output: 4

```

**Example 2:**

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30

```

**Example 3:**

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23

```

**Constraints:**

- `1 <= piles.length <= 104`
- `piles.length <= h <= 109`
- `1 <= piles[i] <= 109`

## Approach 1: Binary search
Time complexity: `O(nlog(k))`    |    Space complexity: `O(1)`
where `n` is the length of `piles` and `k` the max of `piles`

``` python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas/k)
            
            return hours <= h
        
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid -1
            else:
                left = mid + 1
        
        return left
```