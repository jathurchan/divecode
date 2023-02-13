---
date: 2022.11.16
title: 92. Reverse Linked List II
difficulty:
    - medium
runtime: 16.77 # faster than (in %)
memory usage: 51.68    # less than (in %)
---
## Description
Given the `head` of a singly linked list and two integers `left` and `right`where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)

```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

```

**Example 2:**

```
Input: head = [5], left = 1, right = 1
Output: [5]

```

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `500 <= Node.val <= 500`
- `1 <= left <= right <= n`

**Follow up:**

Could you do it in one pass?

## Approach 1:
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the number of nodes

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prev = None
        curr = head
        pos = 1
        
        while pos < left:
            prev = curr
            curr = curr.next
            pos += 1
        
        before_left = prev
        after_right = curr
        
        while curr and pos <= right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            pos += 1
        
        if before_left:
            before_left.next = prev
        else:
            head = prev
        after_right.next = curr
        
        return head
```