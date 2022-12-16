---
date: 2022.12.16
title: 232. Implement Queue using Stacks
difficulty:
    - medium
runtime: 91.33 # faster than (in %)
memory usage: 24.53    # less than (in %)
---
## Description


## Approach 1: 2 Stacks
Time complexity: `O(1)` amortized


``` python
class MyQueue:

    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        self.stackIn.append(x)


    def pop(self) -> int:
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        return self.stackOut.pop()

    def peek(self) -> int:
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
        return self.stackOut[-1]

    def empty(self) -> bool:
        return not self.stackIn and not self.stackOut


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```