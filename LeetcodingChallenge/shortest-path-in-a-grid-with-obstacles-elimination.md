---
date: 2022.11.18
title: 1293. Shortest Path in a Grid with Obstacles Elimination
difficulty:
    - hard
runtime: 5.01 # faster than (in %)
memory usage: 5.12    # less than (in %)
---
## Description
You are given an `m x n` integer matrix `grid` where each cell is either `0` (empty) or `1` (obstacle). You can move up, down, left, or right from and to an empty cell in **one step**.

Return *the minimum number of **steps** to walk from the upper left corner* `(0, 0)` *to the lower right corner* `(m - 1, n - 1)` *given that you can eliminate **at most*** `k` *obstacles*. If it is not possible to find such walk return `-1`.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/09/30/short1-grid.jpg](https://assets.leetcode.com/uploads/2021/09/30/short1-grid.jpg)

```
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) ->(3,2) -> (4,2).

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/09/30/short2-grid.jpg](https://assets.leetcode.com/uploads/2021/09/30/short2-grid.jpg)

```
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 40`
- `1 <= k <= m * n`
- `grid[i][j]` is either `0` **or** `1`.
- `grid[0][0] == grid[m - 1][n - 1] == 0`

## Approach 1: BFS
Time complexity: `O(n*m*k)`    |    Space complexity: `O(n*m*k)`
where `n x m` is the size of `grid` and `k` the number of obstacles that can be eliminated

``` python
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def valid(i, j, remObs):
            return 0 <= i < m and 0 <= j < n and (grid[i][j] == 0 or (grid[i][j] == 1 and remObs > 0))
        
        queue = deque([(0,0,0, k)]) # row, col, steps, remaining obstacles that can be eliminated
        seen = {(0,0,k)}
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        ans = float('inf')
        
        while queue:
            current_length = len(queue)
            
            for _ in range(current_length):
                row, col, steps, remObs = queue.popleft()
                
                if row == m-1 and col == n-1:
                    ans = min(ans, steps)
                
                for di, dj in directions:
                    next_row, next_col = row+di, col+dj
                    
                    if valid(next_row, next_col, remObs) and (next_row, next_col, remObs) not in seen:
                        seen.add((next_row, next_col, remObs))
                        
                        if grid[next_row][next_col] == 0:   # empty
                            queue.append((next_row, next_col, steps+1, remObs))
                        else:
                            queue.append((next_row, next_col, steps+1, remObs-1))
        
        if ans == float('inf'):
            return -1
        else:
            return ans
                
```