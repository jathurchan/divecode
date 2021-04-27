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
        
        # 3. Filling up the "answers" matrix
        for i, j in order:

            val = matrix[i][j]

            ind_of_same = [(i,j)]

            max_rank = 0

            for k in range(m):  # Check Column
                if k != i:
                    if filled[k][j] and matrix[k][j] == val:    # same value already present in the column ?
                        ind_of_same.append((k, j))
                    elif answers[k][j] > max_rank:
                        max_rank = answers[k][j]
            
            for l in range(n):  # Check Row
                if l != j:
                    if filled[i][l] and matrix[i][l] == val:    # same value already present in the column ?
                        ind_of_same.append((i, l))
                    elif answers[i][l] > max_rank:
                        max_rank = answers[i][l]

            for k, l in ind_of_same:
                answers[k][l] = max(max_rank + 1, answers[ind_of_same[-1][0]][ind_of_same[-1][1]])
            filled[i][j] = True
        
        return answers
    

sol = Solution()
print(sol.matrixRankTransform([[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]))