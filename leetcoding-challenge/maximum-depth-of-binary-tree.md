---
date: 2022.11.17
title: 104. Maximum Depth of Binary Tree
difficulty:
    - easy
runtime: 96.03 # faster than (in %)
memory usage: 55.79    # less than (in %)
---
## Description
Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 3

```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `100 <= Node.val <= 100`

## Approach 1: DFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is number of nodes in the binary tree

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```