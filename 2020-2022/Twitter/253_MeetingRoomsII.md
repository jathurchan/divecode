# 253. Meeting Rooms II

## Description

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]

Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]

Output: 1

Constraints:

1 <= intervals.length <= 104

0 <= starti < endi <= 106

## Thoughts

- Sort the intervals by start of intervals
- use a heap to store rooms currently allocated (only the end times are stored in decreasing order)
- pop if the min value of end in heap is smaller than the start time of the current else just push
- length of the heap gives us the result

## Solution

Runtime: 64 ms, faster than 54.29% of Python online submissions for Meeting Rooms II.

Memory Usage: 17.3 MB, less than 14.35% of Python online submissions for Meeting Rooms II.

```python
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        rooms = []
        
        intervals.sort(key=lambda x:x[0])   # sort by start time
        
        heapq.heappush(rooms, intervals[0][1])
        
        for i in intervals[1:]:
            
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, i[1])
        
        return len(rooms)
```

