---
date: 2022.11.16
title: 2130. Maximum Twin Sum of a Linked List
difficulty:
    - medium
runtime: 32.09 # faster than (in %)
memory usage: 72.92    # less than (in %)
---
## Description
In a linked list of size `n`, where `n` is **even**, the `ith` node (**0-indexed**) of the linked list is known as the **twin** of the `(n-1-i)th` node, if `0 <= i <= (n / 2) - 1`.

- For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1`is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum** is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return *the **maximum twin sum** of the linked list*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/12/03/eg1drawio.png](https://assets.leetcode.com/uploads/2021/12/03/eg1drawio.png)

```
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/12/03/eg2drawio.png](https://assets.leetcode.com/uploads/2021/12/03/eg2drawio.png)

```
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.

```

**Example 3:**

![https://assets.leetcode.com/uploads/2021/12/03/eg3drawio.png](https://assets.leetcode.com/uploads/2021/12/03/eg3drawio.png)

```
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

```

**Constraints:**

- The number of nodes in the list is an **even** integer in the range `[2, 105]`.
- `1 <= Node.val <= 105`

## Approach 1: Slow fast pointers (middle then reverse)
Time complexity: `O(n)`    |    Space complexity: `O(1)`


``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Get the pointer to the second middle of the linked list (even length)
        # slow will point to the second middle of the linked list
        
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        
        # Reverse the second part of the linked list
        # prev will point to the last node (reverse linked list)
        
        prev = None
        curr = slow
        
        # remove second part from the first part
        slow = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        second_head = prev
        
        # linked lists (head and sec_head)
        max_twin_sum = 0
        
        while head and second_head:
            
            max_twin_sum = max(max_twin_sum, head.val + second_head.val)
            
            head = head.next
            second_head = second_head.next
        
        return max_twin_sum
```