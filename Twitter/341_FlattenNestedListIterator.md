# 341. Flatten Nested List Iterator

## Description

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List nestedList) Initializes the iterator with the nested list nestedList.

int next() Returns the next integer in the nested list.

boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Your code will be tested with the following pseudocode:

initialize iterator with nestedList

res = []

while iterator.hasNext()
append iterator.next() to the end of res

return res

If res matches the expected flattened list, then your code will be judged as correct.

Example 1:

Input: nestedList = [[1,1],2,[1,1]]

Output: [1,1,2,1,1]

Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: nestedList = [1,[4,[6]]]

Output: [1,4,6]

Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Constraints:

1 <= nestedList.length <= 500

The values of the integers in the nested list is in the range [-106, 106].

## Solution

Runtime: 76 ms, faster than 38.41% of Python online submissions for Flatten Nested List Iterator.

Memory Usage: 19.3 MB, less than 51.56% of Python online submissions for Flatten Nested List Iterator.

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(n_list):
            for n_int in n_list:
                if n_int.isInteger():
                    self.integers.append(n_int.getInteger())
                else:
                    flatten(n_int.getList())
        
        self.integers = []
        self.position = -1
        flatten(nestedList)
        

    def next(self):
        """
        :rtype: int
        """
        self.position += 1
        return self.integers[self.position]
            
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.position + 1 < len(self.integers)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```

