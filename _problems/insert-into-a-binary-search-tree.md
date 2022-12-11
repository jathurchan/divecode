---
date: 2022.11.17
title: 701. Insert into a Binary Search Tree
difficulty:
    - medium
runtime: 86.45 # faster than (in %)
memory usage: 99.81    # less than (in %)
---
## Description
You are given the `root` node of a binary search tree (BST) and a `value` to insert into the tree. Return *the root node of the BST after the insertion*. It is **guaranteed** that the new value does not exist in the original BST.

**Notice** that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return **any of them**.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

```

![https://assets.leetcode.com/uploads/2020/10/05/bst.jpg](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)

**Example 2:**

```
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

```

**Example 3:**

```
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

```

**Constraints:**

- The number of nodes in the tree will be in the range `[0, 104]`.
- `108 <= Node.val <= 108`
- All the values `Node.val` are **unique**.
- `108 <= val <= 108`
- It's **guaranteed** that `val` does not exist in the original BST.

## Approach 1:
Time complexity: `O(h)`    |    Space complexity: `O(h)`
where `h` is the height of the BST

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val, None, None)
        
        if val > root.val:
            return TreeNode(root.val, root.left, self.insertIntoBST(root.right, val))
        else:
            return TreeNode(root.val, self.insertIntoBST(root.left, val), root.right)
```