---
date: 2022.11.15
title: 1832. Check if the Sentence Is Pangram
difficulty:
    - easy
runtime: 5.79 # faster than (in %)
memory usage: 55.09    # less than (in %)
---
## Description
A **pangram** is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return **`true` *if* `sentence` *is a **pangram**, or* `false` *otherwise.*

**Example 1:**

```
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

```

**Example 2:**

```
Input: sentence = "leetcode"
Output: false

```

**Constraints:**

- `1 <= sentence.length <= 1000`
- `sentence` consists of lowercase English letters.

## Approach 1: Array
Time complexity: `O(n)`    |    Space complexity: `O(1)` (26 letters only)
where `n` is the length of `sentence`

``` python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [False]*26
        
        for c in sentence:
            idx = ord(c) - ord('a')
            letters[idx] |= True
        
        for i in range(26):
            if not letters[i]:
                return False
        
        return True
```