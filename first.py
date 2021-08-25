class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        a = 0
        while a * a <= c:
            b = sqrt(c - a * a)
            if int(b) == b:
                return True
            a += 1

        return False

mySol = Solution()
print(mySol.judgeSquareSum(5))