---
date: 2022.12.06
title: 328. Odd Even Linked List
difficulty:
    - medium
runtime: 47.50 # faster than (in %)
memory usage: 78.70    # less than (in %)
---
## Description
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

```

**Constraints:**

- The number of nodes in the linked list is in the range `[0, 104]`.
- `106 <= Node.val <= 106`

## Approach 1: Two pointers (1 for even other for odd)
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the number of nodes

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        even_head = head.next   # head is odd_head

        odd = head
        even = even_head

        curr = even_head.next

        while curr and curr.next:
            
            odd.next = curr
            odd = odd.next

            even.next = curr.next
            even = even.next

            curr = curr.next.next
        
        if curr:
            odd.next = curr
            odd = odd.next
        
        even.next = None
        odd.next = even_head

        return head
```