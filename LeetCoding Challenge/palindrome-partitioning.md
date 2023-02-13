---
date: 2023.01.22
title: 131. Palindrome Partitioning
difficulty:
    - medium
runtime: 64.93 # faster than (in %)
memory usage: 46.86    # less than (in %)
---
## Description
Given a string `s`, partition `s` such that every

substring

of the partition is a

**palindrome**

. Return

*all possible palindrome partitioning of*

```
s
```

.

**Example 1:**

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

```

**Example 2:**

```
Input: s = "a"
Output: [["a"]]

```

**Constraints:**

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Approach 1: Backtracking
Time complexity: `O(n*2^n)`    |    Space complexity: `O(n*2^n)`
where `n` is the length of the string.

``` python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        
        def isPalindrome(ss):
            for i in range(len(ss)//2):
                if ss[i] != ss[len(ss)-1-i]:
                    return False
            return True
        
        def build(i, acc):
            if i == len(s):
                ans.append(acc)
            
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    build(j, acc + [s[i:j]])
        
        build(0, [])
        return ans
```