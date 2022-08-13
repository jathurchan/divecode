# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    235. Lowest Common Ancestor of a Binary Search Tree

    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p
    and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Constraints:

        -   The number of nodes in the tree is in the range [2, 105].
        -   -109 <= Node.val <= 109
        -   All Node.val are unique.
        -   p != q
        -   p and q will exist in the BST.
    """

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        val = root.val
        p_val = p.val
        q_val = q.val

        if (p_val <= val and q_val >= val) or (p_val >= val and q_val <= val):
            return root
        elif p_val < val and q_val < val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)