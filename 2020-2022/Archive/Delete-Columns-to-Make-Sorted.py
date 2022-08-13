class Solution(object):
    """
    944. Delete Columns to Make Sorted

    You are given an array of n strings strs, all of the same length.
    The strings can be arranged such that there is one on each line, making a grid.
    For example, strs = ["abc", "bce", "cae"] can be arranged as:
        abc
        bce
        cae
    You want to delete the columns that are not sorted lexicographically. In the above example
    (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while
    column 1 ('b', 'c', 'a')is not, so you would delete column 1.
    Return the number of columns that you will delete.
    """

    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        n = len(strs)
        length = len(strs[0])

        n_of_cols = 0

        for j in range(length):

            i = 0

            while i < n-1 and strs[i][j] <= strs[i+1][j]:
                i += 1
            
            if i != n - 1:
                n_of_cols += 1
        
        return n_of_cols

sol = Solution()
print(sol.minDeletionSize(["zyx","wvu","tsr"]))