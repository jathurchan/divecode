# 128. Longest Consecutive Sequence

## Description

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

**Input:** nums = [100,4,200,1,3,2]

**Output:** 4

**Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

**Example 2:**

**Input:** nums = [0,3,7,2,5,8,4,6,0,1]

**Output:** 9

**Constraints:**

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

## Thoughts

### First Idea

- A list of consecutive elements can be quickly defined with only the **first element** and the **last element** of the list.
- In each step `i`, check whether a list ends by `nums[i]-1` and an another list begins by `nums[i]+1`
   - If they both exist, merge them both with `nums[i]` in between.
   - If only one of them exist, update the existing list accordingly.
   - Else, create a new list with only `nums[i]`.
- At the end, get the max length by iterating over the built lists

### Second Idea

- Convert the `nums` array into a set
- For each number whose previous number is not in the set, we increase the counter as long as we find consecutive numbers
- At the end of the step, compare the counter with the one in the memory and store only the maximum.

## Solution

- 68 / 70 test cases passed.
- Status: Time Limit Exceeded

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbersPresent = set(nums);
        
        maxLen = 0
        
        for start in nums:
            if start-1 not in nums:
                last = start + 1
                while last in nums:
                    last += 1
                if last-start > maxLen:
                    maxLen = last-start
        
        return maxLen
```

