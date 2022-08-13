# Single Number III

## Description

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in **any order**.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

**Example 1:**

**Input:** nums = [1,2,1,3,2,5]

**Output:** [3,5]

**Explanation: ** [5, 3] is also a valid answer.

**Example 2:**

**Input:** nums = [-1,0]

**Output:** [-1,0]

**Example 3:**

**Input:** nums = [0,1]

**Output:** [1,0]

**Constraints:**

- `2 <= nums.length <= 3 * 104`
- `-231 <= nums[i] <= 231 - 1`
- Each integer in `nums` will appear twice, only two integers will appear once.

## Thoughts

- Using a hashtable that stores the frequency of appearence for each number is not the right choice (because the space complexity is not constant)
- Sorting and then checking at each step 2 consecutive elements is neither ok.
- Using bit manipulation (especially XOR) (Learnt this through the solution given by [umesh72614](https://leetcode.com/umesh72614))
   - Apply `^` between every elements of the integer array (if a same element is repeated, it will disappear) → we would get `a^b` where a and b are the numbers we are searching for.
   - As these 2 numbers are different, they have at least 1 different bit. We can choose the rightmost bit that is different thanks to the formula: `(a^b) & -(a^b)`
   - On the second run, we apply `^` between all numbers that have this bit equal to `1` that would give us `a`.
   - To get B, we can simply perform a ^ (a ^ b).

## Solution

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        aXORb = 0   # Does not affect because a ^ 0 = a
        for nm in nums:
            aXORb ^= nm
        
        rightSetBit = aXORb & -aXORb

        a = 0
        for nm in nums:
            if (rightSetBit & nm):
                a ^= nm
        
        return [a, aXORb^ a]
```

