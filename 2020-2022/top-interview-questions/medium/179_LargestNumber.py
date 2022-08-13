class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        if not any(nums):
            return "0"
        
        def compare(i1, i2):
            if i1+i2>i2+i1:
                return -1
            elif i1+i2<i2+i1:
                return 1
            else:
                return 0
            
        strs = sorted(map(str, nums), cmp=compare)
        
        return "".join(strs)