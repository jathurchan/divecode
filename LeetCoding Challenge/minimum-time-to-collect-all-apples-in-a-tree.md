---
date: 2023.01.11
title: Minimum Time to Collect All Apples in a Tree
difficulty:
    - medium
runtime: 98.72 # faster than (in %)
memory usage: 47.44    # less than (in %)
---
## Description
Given an undirected tree consisting of `n` vertices numbered from `0` to `n-1`, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. *Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at **vertex 0** and coming back to this vertex.*

The edges of the undirected tree are given in the array `edges`, where `edges[i] = [ai, bi]` means that exists an edge connecting the vertices `ai` and `bi`. Additionally, there is a boolean array `hasApple`, where `hasApple[i] = true` means that vertex `i` has an apple; otherwise, it does not have any apple.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_1.png](https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_1.png)

```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_2.png](https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_2.png)

```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

```

**Example 3:**

```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0

```

**Constraints:**

- `1 <= n <= 105`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai < bi <= n - 1`
- `fromi < toi`
- `hasApple.length == n`

## Approach 1: DFS
Time complexity: `O(n)`    |    Space complexity: `O(n)`
where `n` is the number of nodes in the tree.

``` python
from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)  # undirected tree
        
        def dfs(node):

            seen.add(node)   # mark the node as visited
            
            minTime = 0

            for neighbor in graph[node]:
                if neighbor not in seen:
                    temp = dfs(neighbor)
                    if temp>0 or hasApple[neighbor]:
                        minTime += temp + 2
            
            return minTime
        
        seen = set()
        return dfs(0)
```

``` cpp
class Solution {
public:
    unordered_map<int, vector<int>> graph;
    unordered_set<int> seen;

    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        for (vector<int>& edge: edges) {
            int x = edge[0], y = edge[1];
            graph[x].push_back(y);
            graph[y].push_back(x);
        }
        
        return dfs(0,hasApple);

    }

    int dfs(int node, vector<bool>& hasApple) {
        
        seen.insert(node);

        int minTime = 0;

        for (int neighbor: graph[node]) {
            if (seen.find(neighbor) == seen.end()) {    // neighbor not in seen
                
                int temp = dfs(neighbor, hasApple);
                
                if ((temp > 0) || hasApple[neighbor] ) {
                    minTime += (temp + 2);
                }
            }
        }
        

        return minTime;
    }
};
```