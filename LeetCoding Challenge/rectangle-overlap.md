---
date: 2022.11.07
title: 836. Rectangle Overlap
difficulty:
    - easy
runtime: 6.15 # faster than (in %)
memory usage: 68.17    # less than (in %)
---
## Description


## Approach 1: Consider no overlap cases
Time complexity: `O(1)`    |    Space complexity: `O(1)`


``` python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not(rec2[0] >= rec1[2] or
                  rec2[2] <= rec1[0] or
                  rec1[1] >= rec2[3] or
                  rec1[3] <= rec2[1])
```