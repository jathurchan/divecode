class Solution(object):
    """
    1632. Rank Transform of a Matrix
    Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
    The rank is an integer that represents how large an element is compared to other elements. It is calculated
    using the following rules:
        *   The rank is an integer starting from 1.
        *   If two elements p and q are in the same row or column, then:
            -   If p < q then rank(p) < rank(q)
            -   If p == q then rank(p) == rank(q)
            -   If p > q then rank(p) > rank(q)
        *   The rank should be as small as possible.
    It is guaranteed that answer is unique under the given rules.
    """

    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m, n = len(matrix), len(matrix[0])

        # 1. Determine in which order to fill the "answers" matrix
        order = []
        for i in range(m):
            for j in range(n):
                order.append((i,j))

        order = sorted(order, key= lambda ind: matrix[ind[0]][ind[1]])

        # 2. Create and Initialize the "answers" matrix
        answers = [[0] * n for _ in range(m)]

        # 3. Keep track of filled cells in the "answers" matrix
        filled = [[False] * n for _ in range(m)]

        # 4. Get the max rank following a certain column and row
        def get_max_rank(i, j):
            max = 0
            v = matrix[i][j]
            for k in range(m):  # Column j
                if matrix[k][j] != v:
                    if answers[k][j] > max:
                        max = answers[k][j]
            for l in range(n):  # Row i
                if matrix[i][l] != v:
                    if answers[i][l] > max:
                        max = answers[i][l]
            return max
        
        # 5. Filling up the "answers" matrix
        c = 0
        while c < n * m:
            
            i, j = order[c] # current cell indices
            val = matrix[i][j]

            if not filled[i][j]:
                counter = 1
                while c + counter < n * m and matrix[order[c + counter][0]][order[c + counter][1]] == val:
                    counter += 1

                max_rank = 0
                
                for curr in range(c, c+counter):
                    max_rank = max(max_rank, get_max_rank(order[curr][0], order[curr][1]))

                for curr in range(c, c+counter):
                    answers[order[curr][0]][order[curr][1]] = max_rank + 1
                    filled[order[curr][0]][order[curr][1]] = True
            
            c += counter
        
        return answers
    

sol = Solution()
print(sol.matrixRankTransform([[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]]))