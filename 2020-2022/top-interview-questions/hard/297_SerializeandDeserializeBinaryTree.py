# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        # DFS
        
        def dfs_ser(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = dfs_ser(root.left, string)
                string = dfs_ser(root.right, string)
            return string
        
        return dfs_ser(root, '')
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs_des(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            
            curr = l.pop(0)
            
            return TreeNode(curr, dfs_des(l), dfs_des(l))   # l accessed as a reference -> pop affects both left and right
        
        root = dfs_des(data.split(','))
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))