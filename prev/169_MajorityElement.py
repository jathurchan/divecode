class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        maxF = 0
        maxN = -1
        
        for n in freq:
            print(n, freq[n])
            if freq[n] > maxF:
                maxF = freq[n]
                maxN = n
        return maxN