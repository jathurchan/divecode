class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        cols = set()
        rows = set()
        
        m = len(matrix)
        
        if m == 0:
            return matrix
        
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        
        for c in cols:
            for i in range(m):
                matrix[i][c] = 0
        
        for r in rows:
            for j in range(n):
                matrix[r][j] = 0
        
        return matrix