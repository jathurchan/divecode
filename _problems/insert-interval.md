---
date: 2023.01.16
title: 57. Insert Interval
difficulty:
    - medium
runtime: 95.87 # faster than (in %)
memory usage: 52.22    # less than (in %)
---
## Description
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals`is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` *after the insertion*.

**Example 1:**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

```

**Example 2:**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

```

**Constraints:**

- `0 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 105`
- `intervals` is sorted by `starti` in **ascending** order.
- `newInterval.length == 2`
- `0 <= start <= end <= 105`

## Approach 1: Iteration
Time complexity: `O(n)`    |    Space complexity: `O(1)`
where `n` is the number of intervals.

``` python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0

        while (i < len(intervals)) and intervals[i][1] < newInterval[0]:    # ignore intervals before
            i += 1
        
        if (i < len(intervals)) and intervals[i][0] <= newInterval[0]:  # new interval start in an existing interval?
            newInterval[0] = intervals[i][0]
        
        counter = 0
        while (i+counter < len(intervals)) and newInterval[1] > intervals[i+counter][1]:    # new interval end after the current interval
            counter += 1
        
        del intervals[i:i+counter]

        if (i < len(intervals)) and newInterval[1] >= intervals[i][0]:  # new interval end in an existing interval?
            newInterval[1] = intervals[i][1]
            intervals.pop(i)
        
        intervals.insert(i, newInterval)

        return intervals
```