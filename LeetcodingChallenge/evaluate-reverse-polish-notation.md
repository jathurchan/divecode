---
date: 2022.12.17
title: 150. Evaluate Reverse Polish Notation
difficulty:
    - medium
runtime: 98.90 # faster than (in %)
memory usage: 22.27    # less than (in %)
---
## Description


## Approach 1: Stack
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `tokens`.

``` python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(c))
        return stack[0]
```