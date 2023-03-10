---
date: 2022.12.13
title: 931. Minimum Falling Path Sum
difficulty:
    - medium
runtime: 63.84 # faster than (in %)
memory usage: 40.57    # less than (in %)
---
## Description
Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any **falling path**through* `matrix`.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)

```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)

```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

```

**Constraints:**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `100 <= matrix[i][j] <= 100`

## Approach 1: Dynamic Programming
Time complexity: `O(n*n)`    |    Space complexity: `O(1)`
where `n` is the length of matrix.

``` python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        def valid(i, j):
            return 0 <= i < n and 0 <= j < n

        dir = [(1, -1), (1, 0), (1, 1)]

        for row in range(1, n):
            for col in range(n):
                minPrevSum = float('inf')
                for k, l in dir:
                    prev_row, prev_col = row-k, col-l
                    if valid(prev_row, prev_col):
                        minPrevSum = min(minPrevSum, matrix[prev_row][prev_col])
                matrix[row][col] = minPrevSum+matrix[row][col]
        
        res = float('inf')
        for col in range(n):
            res = min(res, matrix[-1][col])
        return res
```