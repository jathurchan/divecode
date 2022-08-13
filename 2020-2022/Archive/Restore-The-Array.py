class Solution(object):
    def numberOfArrays(self, s, k):
        """
        1416. Restore The Array

        A program was supposed to print an array of integers. The program forgot to print whitespaces
        and the array is printed as a string of digits and all we know is that all integers in the array
        were in the range [1, k] and there are no leading zeros in the array.
        Given the string s and the integer k. There can be multiple ways to restore the array.
        Return the number of possible array that can be printed as a string s using the mentioned program.
        The number of ways could be very large so return it modulo 10^9 + 7
        """

        self.n = len(s)
        self.mod = 10**9 + 7
        dp = [-1] * self.n
        return self.dfs(s, k, 0, dp)
    

    def dfs(self, s, k, i, dp):
        
        if i == self.n:     # Found a valid way
            return 1
        
        if s[i] == '0':
            return 0
        
        if dp[i] != -1:   # already calculated
            return dp[i]
        
        res, num = 0, 0

        for j in range(i, self.n):
            num = int(s[i:j+1])

            if num > k:     # no need to go further
                break

            res += self.dfs(s, k, j+1, dp)
            res %= self.mod
        
        dp[i] = res
        return res
