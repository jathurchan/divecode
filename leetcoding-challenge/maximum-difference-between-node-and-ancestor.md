---
date: 2022.11.17
title: 1026. Maximum Difference Between Node and Ancestor
difficulty:
    - medium
runtime: 82.9 # faster than (in %)
memory usage: 20.02    # less than (in %)
---
## Description
Given the `root` of a binary tree, find the maximum value `v` for which there exist **different** nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg)

```
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg)

```
Input: root = [1,null,2,null,0,3]
Output: 3

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 5000]`.
- `0 <= Node.val <= 105`

## Approach 1: DFS
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, minVal, maxVal):
            if node is None:
                return
            
            v = max(abs(maxVal - node.val), abs(node.val - minVal))
            
            if v > self.ans:
                self.ans = v
            
            minVal = min(node.val, minVal)
            maxVal = max(node.val, maxVal)
            
            dfs(node.left, minVal, maxVal)
            dfs(node.right, minVal, maxVal)
        
        self.ans = 0 # distance
        dfs(root, root.val, root.val)
        
        return self.ans
```
