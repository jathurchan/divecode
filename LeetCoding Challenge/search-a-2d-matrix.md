---
date: 2022.11.18
title: 74. Search a 2D Matrix
difficulty:
    - medium
runtime: 23.44 # faster than (in %)
memory usage: 8.65    # less than (in %)
---
## Description
Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/05/mat.jpg](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `104 <= matrix[i][j], target <= 104`

## Approach 1: Binary Search
Time complexity: `O(log(m)+log(n))`    |    Space complexity: `O(1)`
where `m x n` is the size of `matrix`

``` python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        left, right = 0, m*n-1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
```