---
date: 2023.01.18
title: 918. Maximum Sum Circular Subarray
difficulty:
    - medium
runtime: 68.97 # faster than (in %)
memory usage: 43.34    # less than (in %)
---
## Description


## Approach 1: Brute Force
Time complexity: `O(n^2)`    |    Space complexity: `O(1)`


``` python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        maxSum = max(nums)
        while i < 2*n:
            tempSum = nums[i % n]
            counter = 1
            while i+counter < 2*n and counter < n and tempSum > 0:
                tempSum += nums[(i+counter) % n]
                maxSum = max(tempSum, maxSum)
                counter += 1
            i += 1
        return maxSum
```

## Approach 2: Kadane's Algorithm
Time complexity: `O(n)`    |    Space complexity: `O(1)`
``` python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        totalSum = nums[0]
        tempMax = nums[0]
        tempMin = nums[0]
        for i in range(1, len(nums)):
            tempMax = max(nums[i], tempMax + nums[i])
            maxSum = max(maxSum, tempMax)
            tempMin = min(nums[i], tempMin + nums[i])
            minSum = min(minSum, tempMin)
            totalSum += nums[i]
        return max(maxSum, totalSum - minSum) if maxSum > 0 else maxSum
```