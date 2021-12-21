# 256. Paint House

## Description

There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.

Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]

Output: 10

Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.

Minimum cost: 2 + 5 + 3 = 10.

Example 2:

Input: costs = 7,6,2

Output: 2

Constraints:

costs.length == n

costs[i].length == 3

1 <= n <= 100

1 <= costs[i][j] <= 20

## Thoughts

- Brute force algorithm too slow
- Memoization

## Solution

Runtime: 52 ms, faster than 35.23% of Python online submissions for Paint House.

Memory Usage: 13.9 MB, less than 7.20% of Python online submissions for Paint House.

```python
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        n = len(costs)
        
        def paint(i, c):
            if (i, c) in self.memo:
                return self.memo[(i,c)]
            
            total = costs[i][c]
            if i == n-1:
                pass
            elif c == 0:
                total += min(paint(i+1, 1), paint(i+1,2))
            elif c ==1:
                total += min(paint(i+1, 0), paint(i+1,2))
            else:
                total += min(paint(i+1, 0), paint(i+1,1))
            
            self.memo[(i, c)] = total
            return total
        
        if costs == []:
            return 0
        
        self.memo = {}
        return min(paint(0, 0), paint(0,1), paint(0,2))
```

