---
date: 2022.11.17
title: 200. Number of Islands
difficulty:
    - medium
runtime: 84.66 # faster than (in %)
memory usage: 51.10    # less than (in %)
---
## Description
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Approach 1: DFS
Time complexity: `O(m*n)`    |    Space complexity: `O(1)`
where `m x n` is the size of grid

``` python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            for k, l in [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]:
                if 0 <= k < m and 0 <= l < n and grid[k][l] == "1":
                    grid[k][l] = -1
                    dfs(k, l)
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans
```