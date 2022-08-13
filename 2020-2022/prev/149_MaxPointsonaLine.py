class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        
        if n < 2:
            return n
        
        v_lines = {}    # x -> set of points in this vertical line
        lines = {}  # (a,b) -> set of points in this line
        
        for i in range(n):
            for j in range(i+1, n):
                
                xA, yA = points[i][0], points[i][1]
                xB, yB = points[j][0], points[j][1]
                
                if xA == xB:
                    
                    if xA not in v_lines:
                        v_lines[xA] = set()
                        
                    v_lines[xA].add(yA)
                    v_lines[xA].add(yB)
                
                else:
                    
                    a = (yA - float(yB)) / (xA - xB)
                    b = yA - a * xA
                    
                    if (a, b) not in lines:
                        lines[(a, b)] = set()
                    
                    lines[(a,b)].add((xA, yA))
                    lines[(a,b)].add((xB, yB))
        
        maxNumber = 0
        
        for vL in v_lines:
            maxNumber = max(maxNumber, len(v_lines[vL]))
            
        for l in lines:
            maxNumber = max(maxNumber, len(lines[l]))
        
        return maxNumber