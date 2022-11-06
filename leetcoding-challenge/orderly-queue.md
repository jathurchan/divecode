---
date: 2022.11.06
title: 899. Orderly Queue
difficulty:
    - hard
runtime: 100.00 # faster than (in %)
memory usage: 46.15    # less than (in %)
---
## Description
You are given a string `s` and an integer `k`. You can choose one of the first `k` letters of `s` and append it at the end of the string..

Return *the lexicographically smallest string you could have after applying the mentioned step any number of moves*.

**Example 1:**

```
Input: s = "cba", k = 1
Output: "acb"
Explanation:
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

```

**Example 2:**

```
Input: s = "baaca", k = 3
Output: "aaabc"
Explanation:
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".

```

**Constraints:**

- `1 <= k <= s.length <= 1000`
- `s` consist of lowercase English letters.

## Approach 1: Only rotations possible when k=1 else any permutation possible
Time complexity: `O(N^2)`    |    Space complexity: `O(N)`
where `N` is the length of `s`

``` python
class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))

```