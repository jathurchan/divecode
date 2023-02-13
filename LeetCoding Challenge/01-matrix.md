---
date: 2022.11.18
title: 542. 01 Matrix
difficulty:
    - medium
runtime: 11.12 # faster than (in %)
memory usage: 26.49    # less than (in %)
---
## Description
Given an `m x n` binary matrix `mat`, return *the distance of the nearest* `0` *for each cell*.

The distance between two adjacent cells is `1`.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

```

**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 104`
- `1 <= m * n <= 104`
- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.

## Approach 1: BFS
Time complexity: `O(n*m)`    |    Space complexity: `O(1)`


``` python
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1
        
        queue = deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))
        
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        while queue:
            row, col, steps = queue.popleft()
            
            for di, dj in directions:
                next_row, next_col = row+di, col+dj
                if (next_row, next_col) not in seen and isValid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps+1))
                    mat[next_row][next_col] = steps
        
        return mat
```