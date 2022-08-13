class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        visited = set()
        
        while n != 1 and n not in visited:
            
            visited.add(n)
            
            temp = n
            sum = 0
            
            while temp > 0:
                d = temp % 10
                temp //= 10
                sum += (d*d)
            
            n = sum
        
        return n == 1

# Runtime: 24 ms, faster than 57.39% of Python online submissions for Happy Number.
# Memory Usage: 13.6 MB, less than 13.73% of Python online submissions for Happy Number.
