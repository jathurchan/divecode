# 1413 Minimum Value to Get Positive Step by Step Sum

## Description

Given an array of integers `nums`, you start with an initial **positive** value *startValue*.

In each iteration, you calculate the step by step sum of *startValue* plus elements in `nums` (from left to right).

Return the minimum **positive** value of *startValue* such that the step by step sum is never less than 1.

**Example 1:**

**Input:** nums = [-3,2,-3,4,2]

**Output:** 5

**Explanation:** If you choose startValue = 4, in the third iteration your step by step sum is less than 1.

**step by step sum

startValue = 4 | startValue = 5 | nums**                   (4 **-3** ) = 1  | (5 **-3** ) = 2    |  -3

(1 **+2** ) = 3  | (2 **+2** ) = 4    |   2

(3 **-3** ) = 0  | (4 **-3** ) = 1    |  -3

(0 **+4** ) = 4  | (1 **+4** ) = 5    |   4

(4 **+2** ) = 6  | (5 **+2** ) = 7    |   2

**Example 2:**

**Input:** nums = [1,2]

**Output:** 1

**Explanation:** Minimum start value should be positive.

**Example 3:**

**Input:** nums = [1,-2,-3]

**Output:** 5

**Constraints:**

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

## Thoughts

- sv - 3 > 1, sv - 3  +2 > 1, sv -3 + 2 -3 > 1, sv -3 + 2 -3 + 4 > 1
- In each iteration `i`, we add the element `nums[i]` to the sum `nums[0] + ... nums[i-1]`. And, we want sum `nums[0] + ... + nums[i]` + `startValue` > 1 for each `i`.
- Thus, it is clear that finding `min(nums[0] + ... + nums[i]) for i` is enough to answer to the question.
- Minimum `startValue` is equal to `that minimum * -1 + 1` if minimum negative else `1`
- As we start that minimum `minSum = 0`, the first formula `minSum * -1 + 1` is enough.

## Code

```python
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minSum = 0
        sum = 0

        for n in nums:
            sum += n
            if sum < minSum:
                minSum = sum
        
        return minSum * -1 + 1
```

