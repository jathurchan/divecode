---
date: 2022.11.16
title: 771. Jewels and Stones
difficulty:
    - easy
runtime: 53.96 # faster than (in %)
memory usage: 12.17    # less than (in %)
---
## Description
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

**Example 1:**

```
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

```

**Example 2:**

```
Input: jewels = "z", stones = "ZZ"
Output: 0

```

**Constraints:**

- `1 <= jewels.length, stones.length <= 50`
- `jewels` and `stones` consist of only English letters.
- All the characters of `jewels` are **unique**.

## Approach 1:
Time complexity: `O(k+n)`    |    Space complexity: `O(k)`
where `k` is the length of `jewels` and `n` the length of `stones`

``` python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        
        ans = 0
        
        for s in stones:
            if s in jewels:
                ans += 1
        
        return ans
```