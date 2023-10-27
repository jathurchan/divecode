class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findMaxLen(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i-1, j+1   
            return j-i-1
        
        left, right = 0, 0

        for i in range(len(s)):
            odd_length = findMaxLen(i, i)
            if odd_length > right - left + 1:
                dist = odd_length // 2
                left, right = i - dist, i + dist

            even_length = findMaxLen(i, i + 1)
            if even_length > right - left + 1:
                dist = (even_length // 2) - 1
                left, right = i - dist, i + 1 + dist
                
        return s[left:right + 1]
