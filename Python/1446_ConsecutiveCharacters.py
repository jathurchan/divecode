class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxCounter = 1
        
        i, n = 0, len(s)
        
        
        while i < n:
            counter = 1
            while i+counter < n and s[i] == s[i + counter]:
                counter += 1
            if counter > maxCounter:
                maxCounter = counter
            i += counter
        
        return maxCounter