class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        n = len(strs)
        lengths = [len(s) for s in strs]
        
        def isCharInAll(j):
            
            if j >= lengths[0]:
                return False
            
            curr = strs[0][j]
            
            for i in range(n):  # index out of bound for a string?
                if j >= lengths[i] or curr != strs[i][j]:
                    return False
            
            return True
        
        j = 0
        while isCharInAll(j):
            j += 1
        
        return strs[0][:j]