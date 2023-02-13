---
date: 2022.12.01
title: 1704. Determine if String Halves Are Alike
difficulty:
    - easy
runtime: 92.15 # faster than (in %)
memory usage: 77.72    # less than (in %)
---
## Description
You are given a string `s` of even length. Split this string into two halves of equal lengths, and let `a` be the first half and `b` be the second half.

Two strings are **alike** if they have the same number of vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, `'A'`, `'E'`, `'I'`, `'O'`, `'U'`). Notice that `s`contains uppercase and lowercase letters.

Return `true` *if* `a` *and* `b` *are **alike***. Otherwise, return `false`.

**Example 1:**

```
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

```

**Example 2:**

```
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

```

**Constraints:**

- `2 <= s.length <= 1000`
- `s.length` is even.
- `s` consists of **uppercase and lowercase** letters.

## Approach 1: Auxiliary function to count
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the length of `s`

``` python
from collections import defaultdict
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        def countVowels(i, j):
            count = 0
            for k in range(i, j):
                if s[k] in vowels:
                    count += 1
            return count
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        return countVowels(0, len(s)//2) == countVowels(len(s)//2, len(s))
```