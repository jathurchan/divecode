---
date: 2023.01.08
title: 149. Max Points on a Line
difficulty:
    - medium
runtime: 68.50 # faster than (in %)
memory usage: 8.91    # less than (in %)
---
## Description
Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

```

**Constraints:**

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `104 <= xi, yi <= 104`
- All the `points` are **unique**.

## Approach 1: Hash Table
Time complexity: `O(n2)`    |    Space complexity: `O(n)`
where `n` is the number of points.

``` python
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) < 2:
            return len(points)
        
        vLines = {}
        oLines = {}

        def addLine(point1, point2):
            if point1[0] == point2[0]:
                if point1[0] not in vLines:
                    vLines[point1[0]] = set()
                
                vLines[point1[0]].add(point1[1])
                vLines[point1[0]].add(point2[1])
                return
            else:
                a = (point1[1] - point2[1]) / (point1[0] - point2[0])
                b = point1[1] - a*point1[0]

                if (a,b) not in oLines:
                    oLines[(a,b)] = set()
                
                oLines[(a,b)].add((point1[0], point1[1]))
                oLines[(a,b)].add((point2[0], point2[1]))

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                addLine(points[i], points[j])
        
        maxNumber = 0
        for st in vLines.values():
            maxNumber = max(len(st), maxNumber)
        for st in oLines.values():
            maxNumber = max(len(st), maxNumber)
        
        return maxNumber
```