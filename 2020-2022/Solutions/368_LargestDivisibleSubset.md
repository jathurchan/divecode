# 368. Largest Divisible Subset

## Description

Given a set of **distinct** positive integers `nums`, return the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

- `answer[i] % answer[j] == 0`, or
- `answer[j] % answer[i] == 0`

If there are multiple solutions, return any of them.

**Example 1:**

**Input:** nums = [1,2,3]

**Output:** [1,2]

**Explanation:** [1,3] is also accepted.

**Example 2:**

**Input:** nums = [1,2,4,8]

**Output:** [1,2,4,8]

**Constraints:**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2 * 109`
- All the integers in `nums` are **unique**.

## Thoughts

- We can sort A → only have to check `answer[i] % answer[j] == 0` (because `answer[j] < answer[i]`)

## Code

```python
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        s_nums = sorted(nums)   # sorted array

        subsets = [[num] for num in s_nums]

        for i in range(len(s_nums)):
            for j in range(i):
                if s_nums[i] % s_nums[j] == 0 and len(subsets[i]) < len(subsets[j]) + 1:
                    subsets[i] = subsets[j] + [s_nums[i]]
        
        return max(subsets, key=len)
```

