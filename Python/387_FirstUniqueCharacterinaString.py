class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        freq = {}
        
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        
        n = len(s)
        
        for i in range(n):
            if freq[s[i]] == 1:
                return i
        
        return -1