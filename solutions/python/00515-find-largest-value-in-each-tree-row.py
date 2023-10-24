# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = [root]
        while queue:
            rowLen = len(queue)
            rowMax = -float('inf')
            for _ in range(rowLen):
                curr = queue.pop(0)
                rowMax = max(rowMax, curr.val)

                # add nodes of next row
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            ans.append(rowMax)
        
        return ans