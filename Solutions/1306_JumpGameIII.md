# 1306. Jump Game III

## Description

Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach to **any** index with value 0.

Notice that you can not jump outside of the array at any time.

**Example 1:**

**Input:** arr = [4,2,3,0,3,1,2], start = 5

**Output:** true

**Explanation:**

All possible ways to reach at index 3 with value 0 are:

index 5 -> index 4 -> index 1 -> index 3

index 5 -> index 6 -> index 4 -> index 1 -> index 3

**Example 2:**

**Input:** arr = [4,2,3,0,3,1,2], start = 0

**Output:** true

**Explanation:** One possible way to reach at index 3 with value 0 is:

index 0 -> index 4 -> index 1 -> index 3

**Example 3:**

**Input:** arr = [3,0,2,1,2], start = 2

**Output:** false

**Explanation:** There is no way to reach at index 1 with value 0.

**Constraints:**

- `1 <= arr.length <= 5 * 104`
- `0 <= arr[i] < arr.length`
- `0 <= start < arr.length`

## Thoughts

- DFS with the following end cases:
   - new index `i` is out of bounds in which case `False`
   - new index `i` already known to be `False` in which case we ignore it immediately
   - if the value at the new index `i` is 0 return `True`

## Solution

Runtime: 252 ms, faster than 79.23% of Python online submissions for Jump Game III.

Memory Usage: 69.7 MB, less than 11.11% of Python online submissions forJump Game III.

```python
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        n = len(arr)
        
        visited = [False]*n
        
        def DFS(i):
            
            if i >= n or i < 0: # Out of bounds?
                return False
            
            if visited[i]:  # already visited => not this way
                return False
            
            if arr[i] == 0: # canReach !
                return True
            
            visited[i] = True
            
            return DFS(i + arr[i]) or DFS(i - arr[i])
        
        return DFS(start)
```

