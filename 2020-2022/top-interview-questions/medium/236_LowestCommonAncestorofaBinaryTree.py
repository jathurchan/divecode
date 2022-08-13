# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None
        
        def search(r):
            if not r:
                return False
            
            left = search(r.left)
            right = search(r.right)
            
            if (left and right) or ((left or right) and (r == p or r == q)):
                self.ans = r
                
                
            
            return r == p or r == q or left or right    # all elements are unique
        
        search(root)
        return self.ans