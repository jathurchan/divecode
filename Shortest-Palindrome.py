class Solution(object):
    """
        214. Shortest Palindrome

        You are given a string s. You can convert s to a palindrome by adding characters in front of it.
        Return the shortest palindrome you can find by performing this transformation.

        Constraints:

            -   0 <= s.length <= 5 * 104
            -   s consists of lowercase English letters only.
    """
    
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        i, curr = 1, s

        while not self.isPalindrome(curr):
            curr = s[i] + curr
            print(curr)
            i += 1
        
        return curr
    
    def isPalindrome(self, s):
        n = len(s)
        m = n // 2

        for i in range(m):
            if s[i] != s[n-1-i]:
                return False
        
        return True

sol = Solution()
print(sol.shortestPalindrome("abcd"))