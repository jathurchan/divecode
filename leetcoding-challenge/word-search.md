---
date: 2022.11.24
title: 79. Word Search
difficulty:
    - medium
runtime: 45.67 # faster than (in %)
memory usage: 99.77    # less than (in %)
---
## Description
Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/04/word2.jpg](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

```

**Example 3:**

![https://assets.leetcode.com/uploads/2020/10/15/word3.jpg](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

```

**Constraints:**

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

## Approach 1: Backtracking
Time complexity: `O(m x n)`    |    Space complexity: `O(1)`
where `m x n` is the size of the board

``` python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        p = len(word)
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def backtrack(row, col, start):
            
            if self.wordExists:
                return
            
            if start == p:
                self.wordExists = True
                return
            
            if not valid(row, col) or word[start] != board[row][col]:
                return
            
            temp = board[row][col]
            board[row][col] = "#"
            
            for dr, dc in directions:
                nextRow, nextCol = row+dr, col+dc
                backtrack(nextRow, nextCol, start+1)
                
            board[row][col] = temp
            
            return
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.wordExists = False
        
        for i in range(m):
            for j in range(n):
                if self.wordExists:
                    return True
                backtrack(i, j, 0)
        
        return self.wordExists
```