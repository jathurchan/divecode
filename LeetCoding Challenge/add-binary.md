---
date: 2023.02.14
title: 67. Add Binary
difficulty:
    - easy
runtime: 93.95 # faster than (in %)
memory usage: 97.46    # less than (in %)
---
## Description
Given two binary strings `a` and `b`, return *their sum as a binary string*.

**Example 1:**

**Input:** a = "11", b = "1"

**Output:** "100"

**Example 2:**

**Input:** a = "1010", b = "1011"

**Output:** "10101"

**Constraints:**


- `1 <= a.length, b.length <= 104`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.


## Approach 1: str to int (base 2) to bin
Time complexity: `O(1)`    |    Space complexity: `O(1)`


``` python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
```