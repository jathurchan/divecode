# 57. Insert Interval

## Description

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]

Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

Output: [[1,2],[3,10],[12,16]]

Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 104

intervals[i].length == 2

0 <= starti <= endi <= 105

intervals is sorted by starti in ascending order.

newInterval.length == 2

0 <= start <= end <= 105

## Solutions

Runtime: 60 ms, faster than 78.02% of Python online submissions for Insert Interval.

Memory Usage: 17 MB, less than 21.30% of Python online submissions for Insert Interval.

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        i, n = 0, len(intervals)
        
        start, end = newInterval
        
        output = []
        
        while i < n and start > intervals[i][0]:
            output.append(intervals[i])
            i += 1
        
        if not output or output[-1][1] < start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], end)
        
        while i < n:
            interval = intervals[i]
            start,end = interval
            i += 1
            
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        
        return output
```

