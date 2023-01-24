---
date: 2023.01.24
title: 909. Snakes and Ladders
difficulty:
    - medium
runtime: 93.18 # faster than (in %)
memory usage: 33.67    # less than (in %)
---
## Description
You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n2` in a **[Boustrophedon style](https://en.wikipedia.org/wiki/Boustrophedon)** starting from the bottom left of the board (i.e. `board[n - 1][0]`) and alternating direction each row.

You start on square `1` of the board. In each move, starting from square `curr`, do the following:

- Choose a destination square `next` with a label in the range `[curr + 1, min(curr + 6, n2)]`.
    - This choice simulates the result of a standard **6-sided die roll**: i.e., there are always at most 6 destinations, regardless of the size of the board.
- If `next` has a snake or ladder, you **must** move to the destination of that snake or ladder. Otherwise, you move to `next`.
- The game ends when you reach the square `n2`.

A board square on row `r` and column `c` has a snake or ladder if `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`. Squares `1` and `n2` do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do **not** follow the subsequent snake or ladder.

- For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move, your destination square is `2`. You follow the ladder to square `3`, but do **not** follow the subsequent ladder to `4`.

Return *the least number of moves required to reach the square* `n2`*. If it is not possible to reach the square, return* `-1`.

**Example 1:**

![https://assets.leetcode.com/uploads/2018/09/23/snakes.png](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)

```
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

```

**Example 2:**

```
Input: board = [[-1,-1],[-1,3]]
Output: 1

```

**Constraints:**

- `n == board.length == board[i].length`
- `2 <= n <= 20`
- `grid[i][j]` is either `1` or in the range `[1, n2]`.
- The squares labeled `1` and `n2` do not have any ladders or snakes.

## Approach 1: BFS
Time complexity: `O(n^2)`    |    Space complexity: `O(n^2)`
where `n` is the length of the board.

``` python
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def getRowCol(cell):
            row = (n-1) - (cell-1) // n
            col = (cell - 1) % n
            if (n-1-row) % 2 == 1:  # invert order in this row
                col = (n-1) - col
            return row, col

        seen = {1}
        queue = deque([(1, 0)]) # cell, number of moves

        self.ans = float('inf')

        while queue:
            cell, moves = deque.popleft(queue)

            if cell == n*n:
                self.ans = min(self.ans, moves)
            
            for step in range(1, 7):
                nextCell = min(cell+step, n*n)
                nextRow, nextCol = getRowCol(nextCell)

                if board[nextRow][nextCol] != -1:   # use ladder / snake
                    nextCell = board[nextRow][nextCol]

                if nextCell not in seen:
                    seen.add(nextCell)
                    queue.append((nextCell, moves+1))
        
        
        if self.ans == float('inf'):
            return -1
        return self.ans
```

## Approach 2: BFS
Time complexity: `O(n^2)`    |    Space complexity: `O(n^2)`
where `n` is the length of the board.

``` python
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        flatten_board = []
        for i in range(n):
            if i % 2 == 0:
                flatten_board += board[n-1-i]
            else:
                flatten_board += list(reversed(board[n-1-i]))

        n_of_moves = []     # take the min to get the result

        squares_to_visit = [(1, 0)]     # (square number (not index) to visit, number of moves to come here from the start)
        visited_squares_indices = set()

        while squares_to_visit:
            current_square = squares_to_visit.pop(0)

            if current_square[0] == n * n:  # last square ?
                n_of_moves.append(current_square[1])
            else:

                if current_square[0] - 1 not in visited_squares_indices:

                    one_square_selected = False    # To choose only the max square number without ladder (Optimization)

                    for k in range(6):
                        real_k = 6 - k  # Number given by a dice (start with 6 : optimization)
                        next_possible_square_index = current_square[0] - 1 + real_k

                        if next_possible_square_index < n * n: # new possible square in the board ?
                            next_value = flatten_board[next_possible_square_index]
                            if next_value > (next_possible_square_index + 1):    # ladder ?
                                squares_to_visit.append((next_value, current_square[1] + 1))    # Climb directly the ladder
                            elif not(one_square_selected) and next_value == -1:     # have at least one alternative to ladders if possible
                                squares_to_visit.append((next_possible_square_index + 1, current_square[1] + 1))
                                one_square_selected = True
                            elif next_value >= 1 and next_value < (next_possible_square_index + 1):     # snake ?
                                squares_to_visit.append((next_value, current_square[1] + 1))    # Take directly the snake

            visited_squares_indices.add(current_square[0]-1)     # Avoid cycles...

        if not n_of_moves:
            return -1

        min_n_of_moves = n*n

        for number in n_of_moves:
            if number < min_n_of_moves:
                min_n_of_moves = number

        return min_n_of_moves
```
