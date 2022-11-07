---
date: 2022.11.07
title: 1323. Maximum 69 Number
difficulty:
    - easy
runtime: 69.01 # faster than (in %)
memory usage: 64.44    # less than (in %)
---
## Description
You are given a positive integer `num` consisting only of digits `6` and `9`.

Return *the maximum number you can get by changing **at most** one digit (*`6` *becomes* `9`*, and* `9` *becomes* `6`*)*.

**Example 1:**

```
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

```

**Example 2:**

```
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

```

**Example 3:**

```
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

```

**Constraints:**

- `1 <= num <= 104`
- `num` consists of only `6` and `9` digits.

## Approach 1:
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where n is the number of digits in `num`


``` python
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        lst = list(str(num))
        
        n = len(lst)
        
        for i in range(n):
            if lst[i] == '6':
                lst[i] = '9'
                break
        
        res = "".join(lst)
        return int(res)
```