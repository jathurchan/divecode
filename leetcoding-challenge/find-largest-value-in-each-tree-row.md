---
date: 2022.11.17
title: 515. Find Largest Value in Each Tree Row
difficulty:
    - medium
runtime: 69.57 # faster than (in %)
memory usage: 50.62    # less than (in %)
---
## Description
Given the `root` of a binary tree, return *an array of the largest value in each row* of the tree **(0-indexed)**.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg](https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg)

```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

```

**Example 2:**

```
Input: root = [1,2,3]
Output: [1,3]

```

**Constraints:**

- The number of nodes in the tree will be in the range `[0, 104]`.
- `231 <= Node.val <= 231 - 1`

## Approach 1: BFS
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        if root is None:
            return []
        
        queue = deque([root])
        
        while queue:
            row_len = len(queue)
            
            maxValue = float('-inf')
            
            for _ in range(row_len):
                node = queue.popleft()
                
                maxValue = max(node.val, maxValue)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            ans.append(maxValue)
        
        return ans
```