# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        def buildO(l):
            
            if l is None:
                if head:
                    return buildE(head.next)
                else:
                    return None
            
            if l.next is None:
                return ListNode(l.val, buildE(head.next))
            
            return ListNode(l.val, buildO(l.next.next))
        
        
        def buildE(l):
            
            if l is None:
                return None
            
            if l.next is None:
                return ListNode(l.val, None)
            
            return ListNode(l.val, buildE(l.next.next))
        
        return buildO(head)