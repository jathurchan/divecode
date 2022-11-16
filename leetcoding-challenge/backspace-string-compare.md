---
date: 2022.11.16
title: 844. Backspace String Compare
difficulty:
    - easy
runtime: 10.48 # faster than (in %)
memory usage: 74.77    # less than (in %)
---
## Description
Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

```

**Example 2:**

```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

```

**Example 3:**

```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

```

**Constraints:**

- `1 <= s.length, t.length <= 200`
- `s` and `t` only contain lowercase letters and `'#'` characters.

**Follow up:** Can you solve it in `O(n)` time and `O(1)` space?

## Approach 1: Stack
Time complexity: `O(m+n)`    |    Space complexity: `O(m+n)`
where `m` is the length of `s` and `n` the length of `t`

``` python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def get_typed_text(text):
            stack = []
            
            for c in text:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            
            return "".join(stack)
        
        return get_typed_text(s) == get_typed_text(t)
```