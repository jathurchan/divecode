class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        n = len(text1)
        m = len(text2)
        
        LCS = [[0] * (m+1) for _ in range(n+1)] # LCS[i][j] is the longest common subsequence for text1[:i+1] and text2[:j+1]
        
        for i in range(n):
            for j in range(m):
                
                if text1[i] == text2[j]:
                    LCS[i+1][j+1] = LCS[i][j] + 1
                else:
                    LCS[i+1][j+1] = max(LCS[i][j + 1], LCS[i + 1][j])
        
        return LCS[n][m]