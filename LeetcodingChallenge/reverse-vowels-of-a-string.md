---
date: 2022.11.04
title: 345. Reverse Vowels of a String
difficulty:
    - easy
runtime: 27.76 # faster than (in %)
memory usage: 85.41    # less than (in %)
---
## Description
Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Example 1:**

```
Input: s = "hello"
Output: "holle"

```

**Example 2:**

```
Input: s = "leetcode"
Output: "leotcede"

```

**Constraints:**

- `1 <= s.length <= 3 * 105`
- `s` consist of **printable ASCII** characters.

## Approach 1: Two Pointers (Convert to list then swap vowels)
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where n is the length of s

``` python
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        s_lst = list(s)
        i, j = 0, len(s)-1
        
        while i < j:
            if s_lst[i] in vowels and s_lst[j] in vowels:   # need to swap
                temp = s_lst[j]
                s_lst[j] = s_lst[i]
                s_lst[i] = temp
                i += 1
                j -= 1
            else:
                if s_lst[i] not in vowels:
                    i += 1
                if s_lst[j] not in vowels:
                    j -= 1
        
        return "".join(s_lst)
```