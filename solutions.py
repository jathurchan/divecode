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
    
    #   446. Arithmetic Slices II - Subsequence
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # -- Found an interesting solution without DP but does not work when a same number occurs more than 1 time

        n = len(nums)

        if n < 3:   # no arithmetic subsequence possible?
            return 0
        
        nOfArithSub = 0 # number of all the arithmetic subsequences of nums (counter)

        sNums = sorted(nums)    # sort the array
        
        for i in range(n-2):    # position of the 1st number in subsequence
            for j in range(i+1, n-1):   # position of the 2nd number in subsequence

                diffOfArithSub = sNums[j] - sNums[i]  # difference between two consecutive numbers in the arithmetic subsequence (if it exists)

                last_pos = j # position of the last added number into the subsequence
                next_pos = j+1  # postion of the next number that could be added

                while next_pos < n and sNums[next_pos] - sNums[last_pos] <= diffOfArithSub:

                    if sNums[next_pos] - sNums[last_pos] == diffOfArithSub: # (at least 3 elements already checked)
                        last_pos = next_pos
                        nOfArithSub += 1    # add 1 to the counter

                    next_pos += 1

        return nOfArithSub


solution = Solution()
#   print(solution.shiftingLetters("aaa", [1,2,3]))
print(solution.numberOfArithmeticSlices([7,7,7,7,7]))