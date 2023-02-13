---
date: 2022.11.17
title: 199. Binary Tree Right Side View
difficulty:
    - medium
runtime: 81.79 # faster than (in %)
memory usage: 98.28    # less than (in %)
---
## Description
Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/14/tree.jpg](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

```

**Example 2:**

```
Input: root = [1,null,3]
Output: [1,3]

```

**Example 3:**

```
Input: root = []
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        if root is None:
            return ans
        
        queue = deque([root])
        
        while queue:
            nodes_in_current_level = len(queue)
            
            node = None
            
            for _ in range(nodes_in_current_level):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(node.val)
        
        return ans
```