---
date: 2022.11.18
title: 863. All Nodes Distance K in Binary Tree
difficulty:
    - medium
runtime: 63.42 # faster than (in %)
memory usage: 13.47    # less than (in %)
---
## Description
Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return *an array of the values of all nodes that have a distance* `k` *from the target node.*

You can return the answer in **any order**.

**Example 1:**

![https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

```

**Example 2:**

```
Input: root = [1], target = 1, k = 3
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 500]`.
- `0 <= Node.val <= 500`
- All the values `Node.val` are **unique**.
- `target` is the value of one of the nodes in the tree.
- `0 <= k <= 1000`

## Approach 1: Add parent using DFS then BFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`


``` python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node, parent):
            if node is None:
                return
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        queue = deque([target])
        seen = {target}
        distance = 0
        
        while queue and distance < k:
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        
        return [node.val for node in queue]
```