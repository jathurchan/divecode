# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    """
    Given the root of a binary tree, each node has a value from 0 to 25 representing the
    letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.
    Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
    (As a reminder, any shorter prefix of a string is lexicographically smaller: for example,
    "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)
    """

    def convert_v_to_c(self, v):
        return chr(v + ord('a'))

    def smallestFromLeaf(self, root):
        return self.find(root, "")
    
    def find(self, root, acc):

        c = self.convert_v_to_c(root.val)

        if root.left == None and root.right == None:    # Is it a leaf ?
            return c
        
        if root.left == None:
            return self.find(root.right, c + acc) + c
        
        if root.right == None:
            return self.find(root.left, c + acc) + c
        
        left_s = self.find(root.left, c + acc)
        right_s = self.find(root.right, c + acc)

        one, two = left_s + c + acc, right_s + c + acc  # compare whole strings

        if one <= two:
            return left_s + c
        else:
            return right_s + c
        