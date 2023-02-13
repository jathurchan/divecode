---
date: 2023.01.21
title: 93. Restore IP Addresses
difficulty:
    - medium
runtime: 98.42 # faster than (in %)
memory usage: 79.81    # less than (in %)
---
## Description


## Approach 1: Backtracking
Time complexity: `O(3^n)`    |    Space complexity: `O(3^n)`


``` python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def validInteger(content):
            if len(content) == 0 or (content[0] == '0' and len(content) > 1):
                return False
            return 0 <= int(content) <= 255
        
        def backtrack(curr, i):
            if len(curr) == 4:
                if i == len(s):
                    self.ans.append(".".join(curr))
                return
            for k in range(3):
                if k+i < len(s) and validInteger(s[i: i+k+1]):
                    curr.append(s[i:i+k+1])
                    backtrack(curr, i+k+1)
                    curr.pop()
        
        self.ans = []
        backtrack([], 0)
        return self.ans
```