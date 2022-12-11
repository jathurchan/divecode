---
date: 2022.11.10
title: 392. Is Subsequence
difficulty:
    - easy
runtime: 63.45 # faster than (in %)
memory usage: 81.67    # less than (in %)
---
## Description
Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*, or* `false` *otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

**Example 1:**

```
Input: s = "abc", t = "ahbgdc"
Output: true

```

**Example 2:**

```
Input: s = "axc", t = "ahbgdc"
Output: false

```

**Constraints:**

- `0 <= s.length <= 100`
- `0 <= t.length <= 104`
- `s` and `t` consist only of lowercase English letters.

## Approach 1:
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the length of the string `t`

``` python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        
        if m > n:
            return False
        
        i, j = 0, 0
        
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == m
```