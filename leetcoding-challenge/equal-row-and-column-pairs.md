---
date: 2022.11.16
title: 2352. Equal Row and Column Pairs
difficulty:
    - medium
runtime: 81.50 # faster than (in %)
memory usage: 28.90    # less than (in %)
---
## Description
Given a **0-indexed** `n x n` integer matrix `grid`, *return the number of pairs* `(Ri, Cj)` *such that row* `Ri` *and column* `Cj` *are equal*.

A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).

**Example 1:**

![https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg](https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg)

```
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg](https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg)

```
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

```

**Constraints:**

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 105`

## Approach 1: Hashmap
Time complexity: `O(n^2)`    |    Space complexity: `O(n)`


``` python
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counts = defaultdict(int)
        
        for row in grid:
            counts[tuple(row)] += 1
        
        n = len(grid)
        
        ans = 0
        
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            col = tuple(col)
            
            if col in counts:
                ans += counts[col]
        
        return ans
```