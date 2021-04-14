def snakesAndLadders(board):
    """
        909. Snakes and Ladders
        On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting
        from the bottom left of the board, and alternating direction each row.  For example, for
        a 6 x 6 board, the numbers are written as follows:
        You start on square 1 of the board (which is always in the last row and first column).  Each
        move, starting from square x, consists of the following:
        -   You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6,
            provided this number is <= N*N.
                -   (This choice simulates the result of a standard 6-sided die roll: ie.,
                    there are always at most 6 destinations, regardless of the size of the board.)
        -   If S has a snake or ladder, you move to the destination of that snake or ladder.
        Otherwise, you move to S.
        A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The
        destination of that snake or ladder is board[r][c].
        Note that you only take a snake or ladder at most once per move: if the destination to a
        snake or ladder is the start of another snake or ladder, you do not continue moving.  (For
        example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square
        is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)
        Return the least number of moves required to reach square N*N.  If it is not possible, return -1.
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