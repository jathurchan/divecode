# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    """
    530. Minimum Absolute Difference in BST
    
    Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values
    of any two different nodes in the tree.
    """

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        l_bfs = []  # left, root, right (order)

        def search_build(r):
            if r.left:
                search_build(r.left)
            l_bfs.append(r.val)
            if r.right:
                search_build(r.right)
        
        search_build(root)

        min_diff = 999999

        for i in range(len(l_bfs)-1):
            diff = l_bfs[i+1]-l_bfs[i]
            if diff < min_diff:
                min_diff = diff


        