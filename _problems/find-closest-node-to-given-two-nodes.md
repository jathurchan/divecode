---
date: 2023.01.25
title: 2359. Find Closest Node to Given Two Nodes
difficulty:
    - medium
runtime: 87.36 # faster than (in %)
memory usage: 51.15    # less than (in %)
---
## Description
You are given a **directed** graph of `n` nodes numbered from `0` to `n - 1`, where each node has **at most one** outgoing edge.

The graph is represented with a given **0-indexed**array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`. If there is no outgoing edge from `i`, then `edges[i] == -1`.

You are also given two integers `node1` and `node2`.

Return *the **index** of the node that can be reached from both* `node1` *and* `node2`*, such that the **maximum** between the distance from* `node1` *to that node, and from* `node2` *to that node is **minimized***. If there are multiple answers, return the node with the **smallest** index, and if no possible answer exists, return `-1`.

Note that `edges` may contain cycles.

**Example 1:**

![https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-2.png](https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-2.png)

```
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-4.png](https://assets.leetcode.com/uploads/2022/06/07/graph4drawio-4.png)

```
Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.

```

**Constraints:**

- `n == edges.length`
- `2 <= n <= 105`
- `1 <= edges[i] < n`
- `edges[i] != i`
- `0 <= node1, node2 < n`

## Approach 1: BFS / DFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the tree.

``` python
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def computeDistances(node, distances):
            distances[node] = 0
            seen = {node}
            curr, depth = node, 0
            while edges[curr] != -1 and edges[curr] not in seen:
                curr = edges[curr]
                depth += 1
                seen.add(curr)
                distances[curr] = depth
        
        distances1, distances2 = {}, {}
        computeDistances(node1, distances1)
        computeDistances(node2, distances2)

        ans = len(edges)
        ansDist = float('inf')

        for n, d in distances1.items():
            if n in distances2:
                dist = max(d, distances2[n])
                if dist < ansDist:
                    ans = n
                    ansDist = dist
                elif dist == ansDist:
                    if n < ans:
                        ans = n

        if ans == len(edges):
            return -1
        return ans
```