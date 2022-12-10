---
date: 2022.12.10
title: 1339. Maximum Product of Splitted Binary Tree
difficulty:
    - medium
runtime: 15.73 # faster than (in %)
memory usage: 17.49    # less than (in %)
---
## Description
Given the `root` of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return *the maximum product of the sums of the two subtrees*. Since the answer may be too large, return it **modulo** `109 + 7`.

**Note** that you need to maximize the answer before taking the mod and not after taking it.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png](https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png)

```
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png](https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png)

```
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 5 * 104]`.
- `1 <= Node.val <= 104`

## Approach 1: Store subtree sums and sum of all nodes above and on the other side of the ancestors
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in `root`.

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def computeSubtreesSum(node):
            if node is None:
                return 0

            node.sum = node.val + computeSubtreesSum(node.left) + computeSubtreesSum(node.right)

            return node.sum
        
        def computeAboveAndOtherSideSum(node, abOthSum):
            if node is None:
                return
            
            node.abOthSum = abOthSum

            leftSum = node.left.sum if node.left else 0
            rightSum = node.right.sum if node.right else 0

            computeAboveAndOtherSideSum(node.left, abOthSum+rightSum+node.val)
            computeAboveAndOtherSideSum(node.right, abOthSum+leftSum+node.val)

        def getMaxProduct(node):
            if node is None:
                return
            
            self.maxProductOfSums = max(self.maxProductOfSums, node.sum * node.abOthSum)
            getMaxProduct(node.left)
            getMaxProduct(node.right)
        
        self.maxProductOfSums = 0
        
        computeSubtreesSum(root)
        computeAboveAndOtherSideSum(root, 0)
        getMaxProduct(root)

        return self.maxProductOfSums % (10**9 + 7)
```
