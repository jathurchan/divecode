# 108. Convert Sorted Array to Binary Search Tree

## Description

Given an integer array `nums` where the elements are sorted in **ascending order**, convert *it to a **height-balanced** binary search tree*.

A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1:**

![btree1.jpeg](https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg)

**Input:** nums = [-10,-3,0,5,9]

**Output:** [0,-3,9,-10,null,5]

**Explanation:** [0,-10,5,null,-3,null,9] is also accepted:

![btree2.jpeg](https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg)

**Example 2:**

![btree.jpeg](https://assets.leetcode.com/uploads/2021/02/18/btree.jpg)

**Input:** nums = [1,3]

**Output:** [3,1]

**Explanation:** [1,3] and [3,1] are both a height-balanced BSTs.

## Solution

Runtime: 131 ms, faster than 5.70% of Python online submissions for Convert Sorted Array to Binary Search Tree.

Memory Usage: 16.3 MB, less than 19.19% of Python online submissions forConvert Sorted Array to Binary Search Tree.

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def build(l, r):
            
            if l > r:
                return None
            
            m = (l+r)//2
            return TreeNode(nums[m], build(l, m-1), build(m+1, r))
        
        return build(0, len(nums)-1)
```

