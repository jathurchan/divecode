---
date: 2022.11.17
title: 103. Binary Tree Zigzag Level Order Traversal
difficulty:
    - medium
runtime: 88.89 # faster than (in %)
memory usage: 96.12    # less than (in %)
---
## Description
Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

```

**Example 2:**

```
Input: root = [1]
Output: [[1]]

```

**Example 3:**

```
Input: root = []
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `100 <= Node.val <= 100`

## Approach 1: BFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the binary tree

``` python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        if root is None:
            return ans
        
        queue = deque([root])
        
        toReverse = False
        
        while queue:
            
            nOfNodesLevel = len(queue)
            
            temp = []
            
            for _ in range(nOfNodesLevel):
                
                node = queue.popleft()
                
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            if toReverse:
                ans.append(reversed(temp))
            else:
                ans.append(temp)
            
            toReverse = not toReverse
        
        return ans
```