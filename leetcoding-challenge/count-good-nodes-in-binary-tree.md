---
date: 2022.11.17
title: 1448. Count Good Nodes in Binary Tree
difficulty:
    - medium
runtime: 85.85 # faster than (in %)
memory usage: 87.90    # less than (in %)
---
## Description
Given a binary tree `root`, a node *X* in the tree is named **good** if in the path from root to *X* there are no nodes with a value *greater than* X.

Return the number of **good** nodes in the binary tree.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)

```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue aregood.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)

```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

**Example 3:**

```
Input: root = [1]
Output: 1
Explanation: Root is considered asgood.
```

**Constraints:**

- The number of nodes in the binary tree is in the range `[1, 10^5]`.
- Each node's value is between `[-10^4, 10^4]`.

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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                return dfs(node.left, maxVal) + dfs(node.right, maxVal)
        
        return dfs(root, root.val)
```