---
date: 2022.11.16
title: 2342. Max Sum of a Pair With Equal Sum of Digits
difficulty:
    - medium
runtime: 70.41 # faster than (in %)
memory usage: 20.00    # less than (in %)
---
## Description
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109

## Approach 1: Hashmap
Time complexity: `O(nlog(n))`    |    Space complexity: `O(n)`
where `n` is the length of `nums`

``` python
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        def sum_digits(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res
        
        sums_idx = defaultdict(list)
        
        for num in nums:
            sum_num = sum_digits(num)
            sums_idx[sum_num].append(num)
        
        ans = -1
        for key in sums_idx:
            curr = sums_idx[key]
            if len(curr) > 1:
                curr.sort(reverse=True)
                ans = max(ans, curr[0] + curr[1])
        
        return ans
```