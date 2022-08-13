# 43 Multiply Strings

## Description

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

**Example 1:**

**Input:** num1 = "2", num2 = "3"

**Output:** "6"

**Example 2:**

**Input:** num1 = "123", num2 = "456"

**Output:** "56088"

**Constraints:**

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## Thoughts

- To compute the product, multiply digit by digit as taught at school.
- If one of the numbers is equal to 0, product immediately equals to 0.
- Create an array to store the result with the appropriate length (n1+n2 is high enough to avoid overflow)
- Multiply 2 digits and add the "carry" number (got from the previous computation) and get the modulous to keep only the digit.

## Solution

```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if num1 == "0" or num2 == "0":  # Product by 0?
            return "0"

        n1, n2 = len(num1), len(num2)

        res_arr = [0]*(n1+n2)   # array of length n1+n2+1

        for i1 in range(n1-1, -1, -1):
            for i2 in range(n2-1, -1, -1):
                res_arr[i1+i2+1] += int(num1[i1]) * int(num2[i2])  # multiply digit by digit
                res_arr[i1+i2] += res_arr[i1+i2+1] // 10
                res_arr[i1+i2+1] %= 10

        res = ""
        for d in res_arr:
            res += str(d)
        
        i=0
        while i < len(res) and res[i] == "0":   # Eliminate zeroes at the beginning
            i += 1
        
        return res[i:]
```

