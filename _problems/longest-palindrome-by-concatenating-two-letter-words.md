---
date: 2022.11.03
title: 2131. Longest Palindrome by Concatenating Two Letter Words
difficulty:
    - medium
runtime: 9.72 # faster than (in %)
memory usage: 54.38    # less than (in %)
---
## Description
You are given an array of strings `words`. Each element of `words`consists of **two** lowercase English letters.

Create the **longest possible palindrome** by selecting some elements from `words` and concatenating them in **any order**. Each element can be selected **at most once**.

Return *the **length** of the longest palindrome that you can create*. If it is impossible to create any palindrome, return `0`.

A **palindrome** is a string that reads the same forward and backward.

**Example 1:**

```
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

```

**Example 2:**

```
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

```

**Example 3:**

```
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

```

**Constraints:**

- `1 <= words.length <= 105`
- `words[i].length == 2`
- `words[i]` consists of lowercase English letters.

## Approach 1: HashMap to store reversed words

Time complexity: `O(n)` | Space complexity: `O(n)`
where n is the length of `words`

``` python
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        max_len = 0
        waiting_words = {}
        
        for word in words:
            if word in waiting_words:
                max_len += 4
                if waiting_words[word] > 1:
                    waiting_words[word] -= 1
                else:
                    del waiting_words[word]
            else:
                revWord = word[::-1]
                if revWord in waiting_words:
                    waiting_words[revWord] += 1
                else:
                    waiting_words[revWord] = 1
        
        # Add 2 if a string with 2 same characters remains
        # It can be added in the middle of the palindrome word
        for word in waiting_words.keys():
            if word == word[::-1]:
                max_len += 2
                break
        
        return max_len
```