# 96 Unique Binary Search Trees

## Description

Given an integer `n`, return *the number of structurally unique **BST'**s (binary search trees) which has exactly* `n` *nodes of unique values from* `1` *to* `n`.

**Example 1:**

![uniquebstn3.jpeg](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)

**Input:** n = 3

**Output:** 5

**Example 2:**

**Input:** n = 1

**Output:** 1

**Constraints:**

- `1 <= n <= 19`

## Thoughts

- BST (Binary Search Trees): all nodes on the left have values smaller than than the value of the root. And the value of the root is smaller than the values of all nodes on the right.
- Let's consider n = 4, `[1, 2, 3, 4]`
   - First, we have the choice to choose the root of the BST
   - Then, we split the list in 2 parts (a part can be equal to None)
   - And we start again until we have placed all nodes
- We do not look for building the BSTs but just counting them.
- Let's name `num_BST(n)` the number of structurally unique BST's for n. It is clear that `num_BST(n) = sum(num_BST(k) * num_BST(n-1-k))` for `k` between `0 and n-1`.
- Thus, we can use a recursive function to solve this problem.
- Dynamic Programming can be used to improve the algorithm.
- Moreover, thanks to the solution given by [NarutoBaryonMode](https://leetcode.com/NarutoBaryonMode), I improved the algorithm further.

## Solution

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:  # null or single node BST
            return 1
        
        dp = [0]* (n+1) # array that stores the values for each k between 0 and n (Dynamic Programming)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for k in range(0, i//2):
                dp[i] += dp[k] * dp[i-1-k]
            dp[i] *= 2

            if (i % 2 == 1):    # Do not forget i/2 if i is odd
                dp[i] += dp[i//2] * dp[i//2]
        
        return dp[n]

sol = Solution()
print(sol.numTrees(3))
```