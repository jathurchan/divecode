---
date: 2022.11.16
title: 83. Remove Duplicates from Sorted List
difficulty:
    - easy
runtime: 60.49 # faster than (in %)
memory usage: 30.28    # less than (in %)
---
## Description
Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the linked list **sorted** as well*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/01/04/list1.jpg](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)

```
Input: head = [1,1,2]
Output: [1,2]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/01/04/list2.jpg](https://assets.leetcode.com/uploads/2021/01/04/list2.jpg)

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 300]`.
- `100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

## Approach 1: Fast and slow pointers
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the number of nodes

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        
        while slow:
            fast = slow.next
            
            while fast and fast.val == slow.val:
                fast = fast.next
            
            slow.next = fast
            slow = slow.next
        
        return head
```