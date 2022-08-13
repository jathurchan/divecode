class Solution(object):
    """
        1392. Longest Happy Prefix

        A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
        Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

        Constraints:

            -   1 <= s.length <= 105
            -   s contains only lowercase English letters.
    """

    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)

        if n == 1:
            return ""
        
        temp = ""

        for i in range(1, n):
            if s[:i] == s[n-i:]:
                temp = s[:i]
        
        return temp


sol = Solution()
print(sol.longestPrefix("leetcodeleet"))
