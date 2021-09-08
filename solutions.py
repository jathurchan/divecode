class Solution(object):
    
    #   848. Shifting Letters
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """

        n = len(s)
        acc = 0
        finString = ""

        for i in range(n-1, -1, -1):
            acc += shifts[i]
            finString = chr( ( ( (ord(s[i]) - ord('a')) + acc) % 26) + ord('a')) + finString

        return finString

solution = Solution()
print(solution.shiftingLetters("aaa", [1,2,3]))