---
date: 2022.12.02
title: 1657. Determine if Two Strings Are Close
difficulty:
    - medium
runtime: 82.00 # faster than (in %)
memory usage: 43.60    # less than (in %)
---
## Description
Two strings are considered **close** if you can attain one from the other using the following operations:

- Operation 1: Swap any two **existing** characters.
    - For example, `abcde -> aecdb`
- Operation 2: Transform **every** occurrence of one **existing**character into another **existing** character, and do the same with the other character.
    - For example, `aacabb -> bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` *if* `word1` *and* `word2` *are **close**, and* `false` *otherwise.*

**Example 1:**

```
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

```

**Example 2:**

```
Input: word1 = "a", word2 = "aa"
Output: false
Explanation:It is impossible to attain word2 from word1, or vice versa, in any number of operations.

```

**Example 3:**

```
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

```

**Constraints:**

- `1 <= word1.length, word2.length <= 105`
- `word1` and `word2` contain only lowercase English letters.

## Approach 1: Using hashmap (compare keys and values)
Time complexity: `O(n+p)`    |    Space complexity: `O(n+p)`
where `n` is the length of `word1`and `p` is the length of `word2`

``` python
from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        
        for c in word1:
            counts1[c] += 1
        
        for c in word2:
            counts2[c] += 1
            
        
        
        return (counts1.keys() == counts2.keys()) and (sorted(counts1.values()) == sorted(counts2.values()))
```