---
date: 2022.11.15
title: 2225. Find Players With Zero or One Losses
difficulty:
    - medium
runtime: 87.00 # faster than (in %)
memory usage: 59.61    # less than (in %)
---
## Description
You are given an integer array `matches` where `matches[i] = [winneri, loseri]` indicates that the player `winneri` defeated player `loseri` in a match.

Return *a list* `answer` *of size* `2` *where:*

- `answer[0]` is a list of all players that have **not** lost any matches.
- `answer[1]` is a list of all players that have lost exactly **one** match.

The values in the two lists should be returned in **increasing** order.

**Note:**

- You should only consider the players that have played **at least one**match.
- The testcases will be generated such that **no** two matches will have the **same** outcome.

**Example 1:**

```
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

```

**Example 2:**

```
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

```

**Constraints:**

- `1 <= matches.length <= 105`
- `matches[i].length == 2`
- `1 <= winneri, loseri <= 105`
- `winneri != loseri`
- All `matches[i]` are **unique**.

## Approach 1: Hashmaps
Time complexity: `O(nlog(n))`    |    Space complexity: `O(n)`
where `n` is the length of `matches`

``` python
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won = defaultdict(int)
        lost = defaultdict(int)
        
        for match in matches:
            won[match[0]] += 1
            lost[match[1]] += 1
        
        ans1 = []
        
        for player in won:
            if player not in lost:
                ans1.append(player)
        
        ans2 = []
        
        for player, number in lost.items():
            if number == 1:
                ans2.append(player)
        
        return [sorted(ans1), sorted(ans2)]
```