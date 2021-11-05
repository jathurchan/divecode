# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    sum = 0 # Sum of Left Leaves

    def computeSum(self, root, isLeftNode):
        if not root: # empty tree
            return
        
        if not root.left and not root.right: # leef
            if isLeftNode:
                self.sum += root.val
            return
        
        self.computeSum(root.left, True)
        self.computeSum(root.right, False)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.computeSum(root, False)
        return self.sum