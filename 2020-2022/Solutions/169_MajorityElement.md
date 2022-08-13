# 169. Majority Element

## Description

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

**Input:** nums = [3,2,3]

**Output:** 3

**Example 2:**

**Input:** nums = [2,2,1,1,1,2,2]

**Output:** 2

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-231 <= nums[i] <= 231 - 1`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## Solution

Runtime: 136 ms, faster than 80.53% of Python online submissions for Majority Element.

Memory Usage: 14.9 MB, less than 29.02% of Python online submissions forMajority Element.

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        maxF = 0
        maxN = -1
        
        for n in freq:
            print(n, freq[n])
            if freq[n] > maxF:
                maxF = freq[n]
                maxN = n
        return maxN
```

- Another solutions:
   - sort the array and choose `nums[n/2]`
   - Use the Boyer-Moore Majority Vote Algorithm

