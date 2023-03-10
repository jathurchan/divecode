---
date: 2022.11.17
title: 1557. Minimum Number of Vertices to Reach All Nodes
difficulty:
    - medium
runtime: 42.73 # faster than (in %)
memory usage: 78.00    # less than (in %)
---
## Description
Given a **directed acyclic graph**, with `n` vertices numbered from `0` to `n-1`, and an array `edges` where `edges[i] = [fromi, toi]` represents a directed edge from node `fromi` to node `toi`.

Find *the smallest set of vertices from which all nodes in the graph are reachable*. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/07/07/untitled22.png](https://assets.leetcode.com/uploads/2020/07/07/untitled22.png)

```
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation:It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/07/07/untitled.png](https://assets.leetcode.com/uploads/2020/07/07/untitled.png)

```
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation:Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.

```

**Constraints:**

- `2 <= n <= 10^5`
- `1 <= edges.length <= min(10^5, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `0 <= fromi, toi < n`
- All pairs `(fromi, toi)` are distinct.

## Approach 1: Using a graph (hashmap)
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of vertices

``` python
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        
        for i, j in edges:
            graph[i].append(j)
            
        ans = set(graph.keys())
        
        for neighbors in graph.values():
            for neighbor in neighbors:
                if neighbor in ans:
                    ans.remove(neighbor)
        
        return list(ans)
```

## Approach 2: Indegree
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of vertices

``` python
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = [0]*n
        
        for x, y in edges:
            indegree[y] += 1
        
        return [node for node in range(n) if indegree[node] == 0]
```