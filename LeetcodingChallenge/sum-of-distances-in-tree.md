---
date: 2022.12.23
title: 834. Sum of Distances in Tree
difficulty:
    - medium
runtime: [] # faster than (in %)
memory usage: []    # less than (in %)
---
## Description
There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1`edges.

You are given the integer `n` and the array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `ith` node in the tree and all other nodes.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)

```
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg)

```
Input: n = 1, edges = []
Output: [0]

```

**Example 3:**

![https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg)

```
Input: n = 2, edges = [[1,0]]
Output: [1,1]

```

**Constraints:**

- `1 <= n <= 3 * 104`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- The given input represents a valid tree.

## Approach 1: Floyd-Warshall (Time Limit Exceeded)
Time complexity: `O(n^3)`    |    Space complexity: `O(n^2)`
where `n` is the number of nodes in the tree.

``` python
from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        dist = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for a, b in edges:
            dist[a][b] = 1
            dist[b][a] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans = []
        for i in range(n):
           ans.append(sum(dist[i]))
        return ans
```