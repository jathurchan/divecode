class Solution(object):
    def convertOtoB(self, board, i, j):
        if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = 'B'
            self.convertOtoB(board, i-1, j)
            self.convertOtoB(board, i+1, j)
            self.convertOtoB(board, i, j-1)
            self.convertOtoB(board, i, j+1)
            
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        
        
        # Avoid capturing regions on the border
        
        for j in range(n):
            self.convertOtoB(board, 0, j)
            self.convertOtoB(board, m-1, j)
        
        for i in range(m):
            self.convertOtoB(board, i, 0)
            self.convertOtoB(board, i, n-1)
        
        
        # Capture the remaining surrounded regions & rename border regions' cells
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'
        
        return board