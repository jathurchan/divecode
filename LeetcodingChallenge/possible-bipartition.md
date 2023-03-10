---
date: 2022.12.21
title: 886. Possible Bipartition
difficulty:
    - medium
runtime: 84.15 # faster than (in %)
memory usage: 18.7    # less than (in %)
---
## Description
We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

Given the integer `n` and the array `dislikes` where `dislikes[i] = [ai, bi]` indicates that the person labeled `ai` does not like the person labeled `bi`, return `true` *if it is possible to split everyone into two groups in this way*.

**Example 1:**

```
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

```

**Example 2:**

```
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

```

**Example 3:**

```
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

```

**Constraints:**

- `1 <= n <= 2000`
- `0 <= dislikes.length <= 104`
- `dislikes[i].length == 2`
- `1 <= dislikes[i][j] <= n`
- `ai < bi`
- All the pairs of `dislikes` are **unique**.

## Approach 1: Graph with DFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`


``` python
from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        colors = [-1] * n

        def dfs(node, color):
            colors[node] = color

            res = True
            for neighbor in graph[node]:
                if colors[neighbor] == colors[node]:    # found a mismatch
                    return False
                if colors[neighbor] == -1:
                    res = res and dfs(neighbor, 1-color)

            return res
        
        for node in range(n):
            if colors[node] == -1:  # not visited yet
                if not dfs(node, 0):
                    return False
        
        return True

```