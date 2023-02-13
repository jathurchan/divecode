---
date: 2023.01.13
title: 2246. Longest Path With Different Adjacent Characters
difficulty:
    - hard
runtime: 61.54 # faster than (in %)
memory usage: 18.22    # less than (in %)
---
## Description
You are given a **tree** (i.e. a connected, undirected graph that has no cycles) **rooted** at node `0` consisting of `n` nodes numbered from `0` to `n - 1`. The tree is represented by a **0-indexed** array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node `0`is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

Return *the length of the **longest path** in the tree such that no pair of **adjacent** nodes on the path have the same character assigned to them.*

**Example 1:**

![https://assets.leetcode.com/uploads/2022/03/25/testingdrawio.png](https://assets.leetcode.com/uploads/2022/03/25/testingdrawio.png)

```
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2022/03/25/graph2drawio.png](https://assets.leetcode.com/uploads/2022/03/25/graph2drawio.png)

```
Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.

```

**Constraints:**

- `n == parent.length == s.length`
- `1 <= n <= 105`
- `0 <= parent[i] <= n - 1` for all `i >= 1`
- `parent[0] == -1`
- `parent` represents a valid tree.
- `s` consists of only lowercase English letters.

## Approach 1: DFS with heap
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the tree.

``` python
from collections import defaultdict
import heapq
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for child in range(1,len(parent)):  # ignore root
            graph[parent[child]].append(child)
        

        def dfs(node):

            seen.add(node)
            longestPathsSub = []

            for neighbor in graph[node]:
                if s[neighbor] != s[node]:  # not the same character
                    heappush(longestPathsSub, dfs(neighbor))
            
            fstLen, sndLen = 0, 0
            
            if longestPathsSub:
                fstLen = -heappop(longestPathsSub)
            
            if longestPathsSub:
                sndLen = -heappop(longestPathsSub)
            
            self.longestPathTree = max(self.longestPathTree, fstLen+1+sndLen)

            return -(1 + max(fstLen, sndLen))   # return negative value for max heap
        
        self.longestPathTree = 1
        seen = set()
        for i in range(len(parent)):
            if i not in seen:
                dfs(i)

        return self.longestPathTree
```