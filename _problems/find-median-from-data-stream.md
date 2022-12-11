---
date: 2022.11.12
title: 295. Find Median from Data Stream
difficulty:
    - hard
runtime: 45.53 # faster than (in %)
memory usage: 7.57    # less than (in %)
---
## Description
The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `105` of the actual answer will be accepted.

**Example 1:**

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

```

**Constraints:**

- `105 <= num <= 105`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 104` calls will be made to `addNum` and `findMedian`.

**Follow up:**

- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## Approach 1: 2 Heaps
Time complexity: `O(1)`, `O(log(n))`, `O(1)`    |    Space complexity: `O(n)`
where `n` is the number of times addNum is called.

``` python
from heapq import *

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -heappushpop(self.minHeap, num))
        if len(self.maxHeap) > len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        

    def findMedian(self) -> float:  # length of minHeap >=  length of maxHeap
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:   # len(self.minHeap) == len(self.maxHeap)
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```