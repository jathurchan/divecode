# 79. Word Search

## Description

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"

Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"

Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"

Output: false

Constraints:

m == board.length

n = board[i].length

1 <= m, n <= 6

1 <= word.length <= 15

board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?

## Thoughts

- Use 2 for loops to iterate over the letters of the board
- Use backtracking to check whether the solution can be found from a certain `(i,j)`

## Solution

Runtime: 5344 ms, faster than 88.84% of Python online submissions for Word Search.

Memory Usage: 13.5 MB, less than 48.98% of Python online submissions for Word Search.

```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        m, n = len(board), len(board[0])
        
        p = len(word)
        
        def backtrack(w_index, i, j):
            
            if w_index == p:    # word found
                return True
            
            if i>= m or j >=n or i<0 or j<0 or board[i][j] != word[w_index]:
                return False
            
            board[i][j] = '#'   # mark as visited
            
            is_found =  backtrack(w_index+1, i-1, j) or backtrack(w_index+1, i, j-1) or backtrack(w_index+1, i+1, j) or backtrack(w_index+1, i, j+1)
            
            board[i][j] = word[w_index]
            
            return is_found
            
            
        for i in range(m):
            for j in range(n):
                
                if backtrack(0, i, j):
                    return True
        
        return False
```

