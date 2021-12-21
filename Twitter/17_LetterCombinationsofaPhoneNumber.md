# 17. Letter Combinations of a Phone Number

## Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"

Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""

Output: []

Example 3:

Input: digits = "2"

Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4

digits[i] is a digit in the range ['2', '9'].

## Solution

Runtime: 20 ms, faster than 51.54% of Python online submissions for Letter Combinations of a Phone Number.

Memory Usage: 13.7 MB, less than 14.92% of Python online submissions for Letter Combinations of a Phone Number.

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        n = len(digits)
        
        if n == 0:
            return []
        
        hash_map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        
        result = []
        
        def backtrack(index, acc):
            if index == n:
                result.append("".join(acc))
                return
            for c in hash_map[digits[index]]:
                acc.append(c)
                
                backtrack(index+1, acc)
                
                acc.pop()
        
        backtrack(0, [])
        return result
```

