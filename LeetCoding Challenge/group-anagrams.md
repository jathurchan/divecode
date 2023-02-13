---
date: 2022.11.15
title: 49. Group Anagrams
difficulty:
    - medium
runtime: 25.41 # faster than (in %)
memory usage: 25.41    # less than (in %)
---
## Description
Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

```

**Example 2:**

```
Input: strs = [""]
Output: [[""]]

```

**Example 3:**

```
Input: strs = ["a"]
Output: [["a"]]

```

**Constraints:**

- `1 <= strs.length <= 104`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Approach 1: Sorted string as a key in a hashmap
Time complexity: `O(n*mlog(m))`    |    Space complexity: `O(n)`
where `m` is the average length of a string and `n` is the length of `strs`

``` python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            anagrams[str(sorted(s))].append(s)
        
        return anagrams.values()
```