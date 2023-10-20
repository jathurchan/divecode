# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def build(nLst):
            if not nLst:
                return []
            curr = nLst.pop(0)
            if curr.isInteger():
                return [curr] + build(nLst)
            else:
                return build(curr.getList()) + build(nLst)
        
        self.lst = build(nestedList)
        self.i = 0

    
    def next(self) -> int:
        res = self.lst[self.i]
        self.i += 1
        return res
    
    def hasNext(self) -> bool:
        return self.i < len(self.lst) 
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())