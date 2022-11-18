---
date: 2022.11.18
title: 1091. Shortest Path in Binary Matrix
difficulty:
    - medium
runtime: 85.47 # faster than (in %)
memory usage: 24.73    # less than (in %)
---
## Description
Given an `n x n` binary matrix `grid`, return *the length of the shortest **clear path** in the matrix*. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the **top-left** cell (i.e., `(0, 0)`) to the **bottom-right** cell (i.e., `(n - 1, n - 1)`) such that:

- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

The **length of a clear path** is the number of visited cells of this path.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/18/example1_1.png](https://assets.leetcode.com/uploads/2021/02/18/example1_1.png)

```
Input: grid = [[0,1],[1,0]]
Output: 2

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/18/example2_1.png](https://assets.leetcode.com/uploads/2021/02/18/example2_1.png)

```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

```

**Example 3:**

```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

```

**Constraints:**

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j] is 0 or 1`

## Approach 1: BFS
Time complexity: `O(n*n)`    |    Space complexity: `O(n*n)`
where `n` is the length of `grid`

``` python
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]:
            return -1
        
        n = len(grid)
        
        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        
        seen = {(0,0)}
        queue = deque([(0, 0, 1)])    # row, col, steps
        
        directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        
        while queue:
            row, col, steps = queue.popleft()
            
            if (row, col) == (n-1, n-1):
                return steps
            
            for di, dj in directions:
                new_row, new_col = row+di, col+dj
                if isValid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps+1))
        
        return -1
```