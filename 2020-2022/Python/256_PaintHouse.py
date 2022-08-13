class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        n = len(costs)
        
        def paint(i, c):
            if (i, c) in self.memo:
                return self.memo[(i,c)]
            
            total = costs[i][c]
            if i == n-1:
                pass
            elif c == 0:
                total += min(paint(i+1, 1), paint(i+1,2))
            elif c ==1:
                total += min(paint(i+1, 0), paint(i+1,2))
            else:
                total += min(paint(i+1, 0), paint(i+1,1))
            
            self.memo[(i, c)] = total
            return total
        
        if costs == []:
            return 0
        
        self.memo = {}
        return min(paint(0, 0), paint(0,1), paint(0,2))
        
        
                    