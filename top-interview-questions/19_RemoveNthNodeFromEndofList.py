# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        def remove(lst):
            
            if lst is None:
                return None, 0
            
            nextLst, nextD = remove(lst.next)
            
            if nextD == n-1:
                return nextLst, nextD+1
            else:
                return ListNode(lst.val, nextLst), nextD+1
        
        new_head, _ = remove(head)
        
        return new_head