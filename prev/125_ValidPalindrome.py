class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        characters = []
        
        for c in s:
            if c.isalnum():
                characters.append(lower(c))
        
        i, n = 0, len(characters)
        
        if n == 0:
            return True
        
        while i <= (n//2):
            if characters[i] != characters[n-1-i]:
                return False
            i += 1
        
        return True