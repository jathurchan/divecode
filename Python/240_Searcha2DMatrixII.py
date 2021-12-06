class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, n-1   # start from right top corner
        
        while i <= m-1 and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target: # cannot be in this column (because all others higher)
                j -= 1
            else:   # cannot be in this row (because all others smaller)
                i += 1
        
        return False