---
date: 2022.11.16
title: 383. Ransom Note
difficulty:
    - easy
runtime: 82.58 # faster than (in %)
memory usage: 94.21    # less than (in %)
---
## Description
Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote`*can be constructed by using the letters from* `magazine` *and* `false` *otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**

```
Input: ransomNote = "a", magazine = "b"
Output: false

```

**Example 2:**

```
Input: ransomNote = "aa", magazine = "ab"
Output: false

```

**Example 3:**

```
Input: ransomNote = "aa", magazine = "aab"
Output: true

```

**Constraints:**

- `1 <= ransomNote.length, magazine.length <= 105`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Approach 1: Hashmap
Time complexity: `O(m)`    |    Space complexity: `O(1)`
where `m` is the length of `magazine`

``` python
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote):
            return False
        
        counts = defaultdict(int)
        
        for c in magazine:
            counts[c] += 1
        
        for c in ransomNote:
            if c in counts and counts[c] > 0:
                counts[c] -= 1
            else:
                return False
        
        return True
```