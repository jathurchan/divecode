---
date: 2022.12.03
title: 451. Sort Characters By Frequency
difficulty:
    - medium
runtime: 92.63 # faster than (in %)
memory usage: 29.81    # less than (in %)
---
## Description
Given a string `s`, sort it in **decreasing order** based on the **frequency**of the characters. The **frequency** of a character is the number of times it appears in the string.

Return *the sorted string*. If there are multiple answers, return *any of them*.

**Example 1:**

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

```

**Example 2:**

```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

```

**Example 3:**

```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

```

**Constraints:**

- `1 <= s.length <= 5 * 105`
- `s` consists of uppercase and lowercase English letters and digits.

## Approach 1: Counter and sort items
Time complexity: `O(n + klog(k))`    |    Space complexity: `O(n)`
where `n`is the length of `s` and `k` is the number of unique characters (that is `O(1)` as `k <= 26`)

``` python
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        keys = sorted(counts.keys(), key= lambda key:counts[key], reverse=True)
        res = []
        for key in keys:
            for i in range(counts[key]):
                res.append(key)
        
        return "".join(res)
```