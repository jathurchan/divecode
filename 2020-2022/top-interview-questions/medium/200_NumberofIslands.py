class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        numOfIslands = 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == "1":
                    
                    toVisit = [(i, j)]
                    
                    while toVisit:
                        
                        
                        k, l = toVisit.pop()
                        grid[k][l] = "-1"
                        
                        if k-1 >= 0 and grid[k-1][l] == "1":
                            toVisit.append((k-1, l))
                        if l-1 >= 0 and grid[k][l-1] == "1":
                            toVisit.append((k, l-1))
                            print("YES")
                        if k < m-1 and grid[k+1][l] == "1":
                            toVisit.append((k+1, l))
                        if l < n-1 and grid[k][l+1] == "1":
                            toVisit.append((k, l+1))
                    
                    numOfIslands += 1
        
        return numOfIslands