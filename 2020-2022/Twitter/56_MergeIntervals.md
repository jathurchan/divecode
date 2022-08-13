# 56. Merge Intervals

## Description

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]

Output: 1,5

Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104

intervals[i].length == 2

0 <= starti <= endi <= 104

## Thoughts

- Sort all intervals according to the start of an interval
- merge intervals if the end of the preceding interval is after the start of the next interval

## Solution

Runtime: 72 ms, faster than 46.82% of Python online submissions for Merge Intervals.

Memory Usage: 15.9 MB, less than 9.60% of Python online submissions for Merge Intervals.

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        sorted_intervals = sorted(intervals, key=lambda interval:interval[0])
        
        i, n = 0, len(sorted_intervals)
        
        output = []
        
        while i < n:
            
            start = sorted_intervals[i][0]
            end = sorted_intervals[i][1]
            
            counter = 1
            while i+counter < n and sorted_intervals[i+counter][0] <= end:
                end = max(end, sorted_intervals[i+counter][1])
                counter += 1
                
            output.append([start, end])
            i += counter
        
        return output
```

