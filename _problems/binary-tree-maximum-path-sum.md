---
date: 2022.12.11
title: 124. Binary Tree Maximum Path Sum
difficulty:
    - hard
runtime: 96.21 # faster than (in %)
memory usage: 31.96    # less than (in %)
---
## Description
A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return *the maximum **path sum** of any **non-empty** path*.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 3 * 104]`.
- `1000 <= Node.val <= 1000`

## Approach 1: DFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the tree.

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def compute(node):
            if node is None:
                return 0

            leftMaxSum, rightMaxSum = compute(node.left), compute(node.right)
            temp = max(node.val, node.val+leftMaxSum, node.val+rightMaxSum)
            self.maxPathSumVal = max(self.maxPathSumVal, temp, node.val+leftMaxSum+rightMaxSum)

            return temp
        
        self.maxPathSumVal = -1000
        compute(root)

        return self.maxPathSumVal
```