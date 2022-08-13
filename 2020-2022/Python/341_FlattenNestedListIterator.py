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