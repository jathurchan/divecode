---
date: 2022.11.17
title: 530. Minimum Absolute Difference in BST
difficulty:
    - easy
runtime: 65.51 # faster than (in %)
memory usage: 47.31    # less than (in %)
---
## Description
Given the `root` of a Binary Search Tree (BST), return *the minimum absolute difference between the values of any two different nodes in the tree*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg](https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg)

```
Input: root = [4,2,6,1,3]
Output: 1

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg](https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg)

```
Input: root = [1,0,48,null,null,12,49]
Output: 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 104]`.
- `0 <= Node.val <= 105`

**Note:** This question is the same as 783: [https://leetcode.com/problems/minimum-distance-between-bst-nodes/](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

## Approach 1: Inorder DFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the binary search tree

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        minAbsDiff = float('inf')
        
        def dfs(node):
            
            if not node:
                return []
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return left + [node.val] + right
            
        vals = dfs(root)
        
        for i in range(1, len(vals)):
            minAbsDiff = min(minAbsDiff, vals[i] - vals[i-1])
        
        return minAbsDiff
```