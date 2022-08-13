class Solution(object):
    """
    1404. Number of Steps to Reduce a Number in Binary Representation to One

    Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:
        -   If the current number is even, you have to divide it by 2.
        -   If the current number is odd, you have to add 1 to it.
    It's guaranteed that you can always reach to one for all testcases.

    Constraints:
        -   1 <= s.length <= 500
        -   s consists of characters '0' or '1'
        -   s[0] == '1'
    """

    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = int(s[0])

        for d in s[1:]:
            n = 2 * n + int(d)
            
        return self.find_num_of_steps(n, 0)

    def find_num_of_steps(self, n, counter):
        if n == 1:
            return counter
        if n % 2 == 1:  # odd
            return self.find_num_of_steps(n+1, counter+1)
        else:   # even
            return self.find_num_of_steps(n/2, counter+1)

sol = Solution()
print(sol.numSteps("1101"))


