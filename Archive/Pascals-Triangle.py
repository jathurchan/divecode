class Solution(object):
    """
    118. Pascal's Triangle

    Given an integer numRows, return the first numRows of Pascal's triangle.

    Constraints:
        -   1 <= numRows <= 30
    """

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        res = [[1]]

        for i in range(1, numRows):
            temp = [1]

            for j in range(1, i):
                temp.append(res[-1][j-1] + res[-1][j])
            
            temp.append(1)

            res.append(temp)
        
        return res

sol = Solution()
print(sol.generate(5))