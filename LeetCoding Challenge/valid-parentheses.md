---
date: 2022.11.16
title: 20. Valid Parentheses
difficulty:
    - easy
runtime: 10.44 # faster than (in %)
memory usage: 72.25    # less than (in %)
---
## Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false

```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

## Approach 1:
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `s`

``` python
class Solution:
    def isValid(self, s: str) -> bool:
        op_pair = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []
        
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack and stack[-1] == op_pair[c]:
                    stack.pop()
                else:
                    return False
        
        return stack == []
```