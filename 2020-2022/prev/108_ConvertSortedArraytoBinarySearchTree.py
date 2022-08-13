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