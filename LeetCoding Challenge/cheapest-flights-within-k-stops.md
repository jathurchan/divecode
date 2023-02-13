---
date: 2023.01.26
title: 787. Cheapest Flights Within K Stops
difficulty:
    - medium
runtime: 80.5 # faster than (in %)
memory usage: 26.71    # less than (in %)
languages:
    - python
---
## Description
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city `fromi` to city `toi` with cost `pricei`.

You are also given three integers `src`, `dst`, and `k`, return ***the cheapest price** from* `src` *to* `dst` *with at most* `k` *stops.* If there is no such route, return **`-1`.

**Example 1:**

![https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)

```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

```

**Example 2:**

![https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png)

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

```

**Example 3:**

![https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png)

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

```

**Constraints:**

- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= fromi, toi < n`
- `fromi != toi`
- `1 <= pricei <= 104`
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## Approach 1: BFS
Time complexity: `O(e*k+n)`    |    Space complexity: `O(e*k+n)`
where `e` is the number of edges and `n` is the number of nodes.

``` python
from collections import deque
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = {}
        graph = defaultdict(list)
        for fr, to, price in flights:
            graph[fr].append(to)
            prices[(fr, to)] = price
        
        cumPrices = [float('inf')]*n
        queue = deque([(src, 0)])  # current city and current price
        remStops = k

        while remStops >= 0 and queue:
            currentDepth = len(queue)

            for _ in range(currentDepth):
                currCity, currPrice = queue.popleft()
                
                for neighbor in graph[currCity]:
                    neighborPrice = currPrice+prices[(currCity, neighbor)]
                    if neighborPrice < cumPrices[neighbor]:
                        queue.append((neighbor, neighborPrice))
                        cumPrices[neighbor] = neighborPrice

            remStops -= 1
        
        if cumPrices[dst] == float('inf'):
            return -1
        return cumPrices[dst]
```