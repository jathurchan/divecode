# 547. Number of Provinces

## Description

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]

Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]

Output: 3

Constraints:

1 <= n <= 200

n == isConnected.length

n == isConnected[i].length

isConnected[i][j] is 1 or 0.

isConnected[i][i] == 1

isConnected[i][j] == isConnected[j][i]

## Thoughts

- DFS

## Solution

Runtime: 164 ms, faster than 60.36% of Python online submissions for Number of Provinces.

Memory Usage: 14.2 MB, less than 15.46% of Python online submissions for Number of Provinces.

```python
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        n = len(isConnected)
        
        visited = [False]*n
        count = 0
        
        def dfs(idx):
            for j in range(n):
                if isConnected[idx][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        
        return count
```

