---
date: 2022.11.15
title: 1941. Check if All Characters Have Equal Number of Occurrences
difficulty:
    - easy
runtime: 76.09 # faster than (in %)
memory usage: 28.83    # less than (in %)
---
## Description
Given a string `s`, return `true` *if* `s` *is a **good** string, or* `false` *otherwise*.

A string `s` is **good** if **all** the characters that appear in `s` have the **same**number of occurrences (i.e., the same frequency).

**Example 1:**

```
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

```

**Example 2:**

```
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Approach 1:
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `s`

``` python
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        
        for c in s:
            counts[c] += 1
        
        base = counts[s[-1]]
        
        for freq in counts.values():
            if freq != base:
                return False
        
        return True
```