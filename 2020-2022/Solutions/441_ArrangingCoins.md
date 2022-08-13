# 441 Arranging Coins

# Description

You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k`rows where the `ith` row has exactly `i` coins. The last row of the staircase **may be** incomplete.

Given the integer `n`, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

![arrangecoins1-grid.jpeg](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg)

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2.

**Example 2:**

![arrangecoins2-grid.jpeg](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg)

**Input:** n = 8

**Output:** 3

**Explanation:** Because the 4th row is incomplete, we return 3.

**Constraints:**

- `1 <= n <= 231 - 1`

# Thoughts

- Exhaustive Iteration:
   - Initialize a variable `rem`  with `n` where `rem` stands for remaining coins
   - Use a while loop with the condition `rem - k >= 0` where k is an integer that starts at 1 and is incremented by 1 at each step.
   - At the end, return `k-1` as the result
- Using Math
   - Find the maximum integer $$l$$ such that $$\frac{l(l+1)}{2} = N$$
   - Thus, we get $$l^2 + l = 2N$$
   - Given $$l^2 + l = (l-\frac{1}{2})^2 - \frac{1}{4}$$, we get $$-\sqrt{2N + \frac{1}{4}} - \frac{1}{2} \leq l \leq \sqrt{2N + \frac{1}{4}} - \frac{1}{2}$$.
   - As we are searching for the maximum l, we immediately get $$l = E( \sqrt{2N + \frac{1}{4}} - \frac{1}{2})$$

   ## Algorithm

```python
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((2* n + 0.25)**0.5 - 0.5)
```

