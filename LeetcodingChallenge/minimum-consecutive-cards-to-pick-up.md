---
date: 2022.11.15
title: 2260. Minimum Consecutive Cards to Pick Up
difficulty:
    - medium
runtime: 23.95 # faster than (in %)
memory usage: 80.06    # less than (in %)
---
## Description
You are given an integer array `cards` where `cards[i]` represents the **value**of the `ith` card. A pair of cards are **matching** if the cards have the **same**value.

Return *the **minimum** number of **consecutive** cards you have to pick up to have a pair of **matching** cards among the picked cards.* If it is impossible to have matching cards, return `-1`.

**Example 1:**

```
Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

```

**Example 2:**

```
Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

```

**Constraints:**

- `1 <= cards.length <= 105`
- `0 <= cards[i] <= 106`

## Approach 1: Hashmap
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `cards`

``` python
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        n = len(cards)
        
        prev = {}
        
        minNum = n+1
        
        for i in range(n):
            if cards[i] in prev:
                temp = i - prev[cards[i]] + 1
                if temp < minNum:
                    minNum = temp
            
            prev[cards[i]] = i
        
        if minNum == n+1:
            return -1
        else:
            return minNum
```