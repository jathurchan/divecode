# 149. Max Points on a Line

## Description

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

**Example 1:**

![plane1.jpeg](https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg)

**Input:** points = [[1,1],[2,2],[3,3]]

**Output:** 3

**Example 2:**

![plane2.jpeg](https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg)

**Input:** points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

**Output:** 4

**Constraints:**

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-104 <= xi, yi <= 104`
- All the `points` are **unique**.

## Thoughts

- A line is uniquely defined by 2 parameters `a` and `b` where a is the slope and b the offset.
- A pair of points is to define a line.
- Iterate over the points using 2 for loops.
- For each pair of points,  calculate `a` and `b` of the line defined by these points. Add these points to the the line defined by `(a, b)` by using a hash table.
- `a = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])`
- `b = points[i][1] - a * points[i][0]`
- Deal with the vertical lines where `points[i][0] = points[j][0]`

## Solution

Runtime: 52 ms, faster than 54.87% of Python online submissions for Max Points on a Line.

Memory Usage: 16.2 MB, less than 7.96% of Python online submissions for Max Points on a Line.

```python
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        
        if n < 2:
            return n
        
        v_lines = {}    # x -> set of points in this vertical line
        lines = {}  # (a,b) -> set of points in this line
        
        for i in range(n):
            for j in range(i+1, n):
                
                xA, yA = points[i][0], points[i][1]
                xB, yB = points[j][0], points[j][1]
                
                if xA == xB:
                    
                    if xA not in v_lines:
                        v_lines[xA] = set()
                        
                    v_lines[xA].add(yA)
                    v_lines[xA].add(yB)
                
                else:
                    
                    a = (yA - float(yB)) / (xA - xB)
                    b = yA - a * xA
                    
                    if (a, b) not in lines:
                        lines[(a, b)] = set()
                    
                    lines[(a,b)].add((xA, yA))
                    lines[(a,b)].add((xB, yB))
        
        maxNumber = 0
        
        for vL in v_lines:
            maxNumber = max(maxNumber, len(v_lines[vL]))
            
        for l in lines:
            maxNumber = max(maxNumber, len(lines[l]))
        
        return maxNumber
```

