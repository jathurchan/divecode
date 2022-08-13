class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        aXORb = 0   # Does not affect because a ^ 0 = a
        for nm in nums:
            aXORb ^= nm
        
        rightSetBit = aXORb & -aXORb

        a = 0
        for nm in nums:
            if (rightSetBit & nm):
                a ^= nm
        
        return [a, aXORb^ a]