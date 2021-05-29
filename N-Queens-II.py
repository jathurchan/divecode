class Solution(object):
    """
        N-Queens II

        The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
        Given an integer n, return the number of distinct solutions to the n-queens puzzle.

        Constraints:
            -   1 <= n <= 9
    """

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        usd_cols, usd_d1, usd_d2 = set(), set(), set()

        return self.count(n, usd_cols, usd_d1, usd_d2, 0)
    
    def count(self, n, cols, d1, d2, row):
        if row == n:
            return 1
        
        count = 0

        for col in range(n):
            if col+row in d1 or row-col in d2 or col in cols:
                continue
            
            d1.add(col+row)
            d2.add(row-col)
            cols.add(col)

            count += self.count(n, cols, d1, d2, row+1)

            d1.remove(col+row)
            d2.remove(row-col)
            cols.remove(col)

        return count


sol = Solution()
print(sol.totalNQueens(4))