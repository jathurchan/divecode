---
date: 2022.11.17
title: 695. Max Area of Island
difficulty:
    - medium
runtime: 35.43 # faster than (in %)
memory usage: 37.97    # less than (in %)
---
## Description
You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

```

**Example 2:**

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.

## Approach 1:
Time complexity: `O(m*n)`    |    Space complexity: `O(1)`
where `m x n` is the size of `grid`

``` python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1
        
        def dfs(i,j):
            if not isValid(i,j):
                return 0
            
            grid[i][j] = 0
            
            ans = 1
            for k, l in [(i, j-1), (i-1, j), (i, j+1), (i+1,j)]:
                    ans += dfs(k, l)
            
            return ans
        
        maxArea = 0
        
        for i in range(m):
            for j in range(n):
                area = dfs(i,j)
                if area > maxArea:
                    maxArea = area
        
        return maxArea
```