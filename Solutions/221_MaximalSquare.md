# 221. Maximal Square

## Description

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, *find the largest square containing only* `1`'s *and return its area*.

**Example 1:**

![max1grid.jpeg](https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg)

**Input:** matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

**Output:** 4

**Example 2:**

![max2grid.jpeg](https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg)

**Input:** matrix = [["0","1"],["1","0"]]

**Output:** 1

**Example 3:**

**Input:** matrix = "0"

**Output:** 0

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is `'0'` or `'1'`.

## Thoughts

- Iterate over the matrix using 2 for loops.
- Use a dp matrix `dp` of the same size as `matrix` where `dp[i][j]` stores the side length of the largest square whose right bottom corner is `matrix[i][j]`.
- It is clear that the size of a square can be retrieved quickly: `sqrt(area) = side`.
- if `matrix[i][j] == 1`, we can get the largest square ending at `(i,j)` by `min(dp[i-1,j], dp[i-1, j-1], dp[i],j-1]) + 1`.

## Solution

Runtime: 214 ms, faster than 36.56% of Python online submissions for Maximal Square.

Memory Usage: 22.1 MB, less than 67.07% of Python online submissions forMaximal Square.

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        maxSideLen = 0
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i][j-1], dp[i-1][j-1]), dp[i-1][j]) + 1
                    maxSideLen = max(dp[i][j], maxSideLen)
                    
        return maxSideLen * maxSideLen
```

