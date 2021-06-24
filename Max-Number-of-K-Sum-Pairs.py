class Solution(object):
    """
        1679. Max Number of K-Sum Pairs

        You are given an integer array nums and an integer k.
        In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
        Return the maximum number of operations you can perform on the array.

        Constraints:
            -   1 <= nums.length <= 105
            -   1 <= nums[i] <= 109
            -   1 <= k <= 109
    """

    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq = {}

        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
        
        max_n_ops = 0

        visited = set()

        for fst in freq.keys():
            if fst not in visited:
                snd = k - fst

                if snd in freq:
                    if fst == snd:
                        max_n_ops += (freq[fst] // 2)
                    else:
                        max_n_ops += (min(freq[fst], freq[snd]))
                    
                    visited.add(snd)

                visited.add(fst)
        
        return max_n_ops

sol = Solution()
print(sol.maxOperations([3,1,3,4,3], 6))


        