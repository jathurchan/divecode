---
date: 2022.11.17
title: 236. Lowest Common Ancestor of a Binary Tree
difficulty:
    - medium
runtime: 81.62 # faster than (in %)
memory usage: 83.57    # less than (in %)
---
## Description
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q`as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![https://assets.leetcode.com/uploads/2018/12/14/binarytree.png](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2018/12/14/binarytree.png](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

```

**Example 3:**

```
Input: root = [1,2], p = 1, q = 2
Output: 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 105]`.
- `109 <= Node.val <= 109`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

## Approach 1: DFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the binary tree

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            
            if node is None:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            
            if left:
                return left
            
            return right
        
        return dfs(root)
```