class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        
        fst2 = {}
        
        for el1 in nums1:
            for el2 in nums2:
                mySum = el1 + el2
                
                if mySum not in fst2:
                    fst2[mySum] = 1
                else:
                    fst2[mySum] += 1
        
        result = 0
        
        for el3 in nums3:
            for el4 in nums4:
                temp = - el3 - el4
                if temp in fst2:
                    result += fst2[temp]
        
        return result