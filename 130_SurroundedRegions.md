# 130 Surrounded Regions

# Description

Given an `m x n` matrix `board` containing `'X'` and `'O'`, *capture all regions that are 4-directionally surrounded by* `'X'`.

A region is **captured** by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example 1:**

![xogrid.jpeg](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:** Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

**Example 2:**

**Input:** board = "X"

**Output:** "X"

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.

# Thoughts

- As surrounded regions should not be on the border, temporarily convert each cell from border regions to some other character (`'B'` for example).
- Use 2 for loops to go through the cells of the board, and convert all remaining `'O'`s into `'X'` and all `'B'`s to `'O'`.

## Complexity

- Time: O(n * m) (*Even though more than just 2 for loops*)
- Space: O(n * m) (*everything is done on the board*)

## Solution

```python
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
```