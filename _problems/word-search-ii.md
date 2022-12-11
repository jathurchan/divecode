---
date: 2022.11.05
title: 212. Word Search II
difficulty:
    - hard
---
## Description
Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example 1:**

![https://assets.leetcode.com/uploads/2020/11/07/search1.jpg](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2020/11/07/search2.jpg](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

```

**Constraints:**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter.
- `1 <= words.length <= 3 * 104`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are unique.

## Approach 1: DFS (Time Limit Exceeded)

``` python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m, n = len(board), len(board[0])
        
        result = []
        
        def dfs(i, j, rem_word):
            
            if len(rem_word) == 0:
                return True
            
            if i<0 or i >= m or j<0 or j>=n or board[i][j] != rem_word[0]:
                return False
            
            # board[i][j] == first character of the remaining word
            
            temp = board[i][j]
            new_word = rem_word[1:]
            board[i][j] = '#'
            # explore through all neighbours (not yet visited)
            res = dfs(i-1, j, new_word) or dfs(i+1, j, new_word) \
            or dfs(i, j-1, new_word) or dfs(i, j+1, new_word)
            board[i][j] = temp
            
            return res
        
        def canAdd(word):
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, word):
                        return True
            return False
        
        for word in words:
            if canAdd(word):
                result.append(word)
         
        return result
```