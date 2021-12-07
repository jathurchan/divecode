# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):    
        """
        :type head: ListNode
        :rtype: int
        """
        
        result = 0
        
        # ----  1st Solution

        # while head:
        #     result = 2 * result + head.val
        #     head = head.next

        # ---- 2nd Solution

        while head:
            result = (result<<1) + head.val
            head = head.next
        
        return result