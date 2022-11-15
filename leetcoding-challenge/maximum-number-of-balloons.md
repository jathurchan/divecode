---
date: 2022.11.15
title: 1189. Maximum Number of Balloons
difficulty:
    - easy
runtime: [] # faster than (in %)
memory usage: []    # less than (in %)
---
## Description
Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

**Example 1:**

![https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG](https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG)

```
Input: text = "nlaebolko"
Output: 1

```

**Example 2:**

![https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG](https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG)

```
Input: text = "loonbalxballpoon"
Output: 2

```

**Example 3:**

```
Input: text = "leetcode"
Output: 0

```

**Constraints:**

- `1 <= text.length <= 104`
- `text` consists of lower case English letters only.

## Approach 1: hashmap
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the length of `text`

``` python
from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        
        for c in text:
            counts[c] += 1
        
        minFreq = counts["b"]
        
        for c in "an":
            if counts[c] < minFreq:
                minFreq = counts[c]
        
        for c in "lo":
            if (counts[c] // 2) < minFreq:
                minFreq = counts[c] // 2
        
        return minFreq
```