---
date: 2023.01.09
title: 144. Binary Tree Preorder Traversal
difficulty:
    - easy
runtime: 99.88 # faster than (in %)
memory usage: 57.18    # less than (in %)
---
## Description
Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
Input: root = [1,null,2,3]
Output: [1,2,3]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [1]
Output: [1]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## Approach 1: Recursion
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where 'n' is the number of nodes.

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

``` cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorder(root, res);
        return res;
    }
    
    void preorder(TreeNode* root, vector<int>& res) {
        if (root == nullptr) {
            return;
        }
        res.push_back(root->val);
        preorder(root->left, res);
        preorder(root->right, res);
    }
};
```

## Approach 2: Iteration
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where 'n' is the number of nodes.

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        stack, res = [root], []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return res
```