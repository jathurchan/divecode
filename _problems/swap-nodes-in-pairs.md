---
date: 2022.11.16
title: 24. Swap Nodes in Pairs
difficulty:
    - medium
runtime: 55.09 # faster than (in %)
memory usage: 65.94    # less than (in %)
---
## Description
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

**Example 1:**

![https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

```
Input: head = [1,2,3,4]
Output: [2,1,4,3]

```

**Example 2:**

```
Input: head = []
Output: []

```

**Example 3:**

```
Input: head = [1]
Output: [1]

```

**Constraints:**

- The number of nodes in the list is in the range `[0, 100]`.
- `0 <= Node.val <= 100`

## Approach 1: Using a prev pointer
Time complexity: `O(n)`    |    Space complexity: `O(1)`


``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        mem = head.next
        prev = None
        
        while head and head.next:
            
            if prev:
                prev.next = head.next
            prev = head
            
            nextNode = head.next.next
            head.next.next = head
            
            head.next = nextNode
            head = nextNode
            
        return mem
```