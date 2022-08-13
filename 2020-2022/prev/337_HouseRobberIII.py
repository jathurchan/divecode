# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def rob(self, root):    # 1st Solution (TIME LIMIT EXCEEDED)
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def rob(r):
            
            if r is None:
                return 0
            
            valRNotRobbed = rob(r.left) + rob(r.right)
            
            valRRobbed = r.val
            
            if r.left:
                valRRobbed += (rob(r.left.left) + rob(r.left.right))
            
            if r.right:
                valRRobbed += (rob(r.right.left) + rob(r.right.right))
            
            return max(valRRobbed, valRNotRobbed)
        
        return rob(root)
    
    def rob2(self, root):   # 2nd Solution
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def compute(r):
            if r is None:
                return [0, 0]
            
            left = compute(r.left)
            right = compute(r.right)
            
            temp = [0, 0]
            
            temp[0] = max(left[0], left[1]) + max(right[0], right[1])
            temp[1] = r.val + left[0] + right[0]
            
            return temp
            
        res = compute(root)
        return max(res[0], res[1])