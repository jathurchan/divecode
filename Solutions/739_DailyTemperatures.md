# 739. Daily Temperatures

## Description

Given an array of integers `temperatures` represents the daily temperatures, return *an array*`answer` *such that* `answer[i]` *is the number of days you have to wait after the* `ith` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0`instead.

**Example 1:**

**Input:** temperatures = [73,74,75,71,69,72,76,73]

**Output:** [1,1,4,2,1,1,0,0]

**Example 2:**

**Input:** temperatures = [30,40,50,60]

**Output:** [1,1,1,0]

**Example 3:**

**Input:** temperatures = [30,60,90]

**Output:** [1,1,0]

**Constraints:**

- `1 <= temperatures.length <= 105`
- `30 <= temperatures[i] <= 100`

## Thoughts

- When `temperatures[i] < temperatures[i+1]`, `answer[i]` is immediately equal to `1`
- if `i == length(temperatures)-1`, `answer[i] = 0`
- Use a stack to store `i` when `temperatures[i] >= temperatures[i+1]`
   - if stack not empty, compare the `temperatures[i]` with `temperatures[stack[-1]]`.
   - while the last element of the stack is lesser than `temperatures[i]`, modify `answers[stack[-1]]` by `i - stack[-1]`.
   - For example, if `temperatures = [73,74,75,71,69,72,76,73]`, 4th element then 5th element are stored in the stack. When exploring the 6th element, 4th element of `answers` would be changed by `5 - 3 = 2` and the 3rd element would be changed  later by `6 - 2 = 4`. Thus, the formula given above seems to work.

## Code

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)

        answers = [0] * n

        stack = []

        for i in range(n-1):
            
            if temperatures[i] < temperatures[i+1]:
                answers[i] = 1
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answers[j] = i - j
            
            if temperatures[i] >= temperatures[i+1]:
                stack.append(i)
        

        while stack and temperatures[stack[-1]] < temperatures[n-1]:    # the last element has to be compared with other elements in the stack
                j = stack.pop()
                answers[j] = n-1 - j
        
        # do not care about the numbers that do not get values above them in the array because initialized with 0
        return answers
```

