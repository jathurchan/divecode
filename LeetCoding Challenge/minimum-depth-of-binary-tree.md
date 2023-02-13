---
date: 2022.11.17
title: 111. Minimum Depth of Binary Tree
difficulty:
    - easy
runtime: 5.01 # faster than (in %)
memory usage: 54.90    # less than (in %)
---
## Description
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 2

```

**Example 2:**

```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 105]`.
- `1000 <= Node.val <= 1000`

## Approach 1:
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the binary tree

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(node):
            if node is None:
                return float('inf')
            
            if node.left is None and node.right is None:
                return 1
            
            return 1 + min(dfs(node.left), dfs(node.right))
        
        return dfs(root)
```