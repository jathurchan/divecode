class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find the rotation index
        
        lo, hi = 1, len(nums)-1
        
        while lo < hi:
            
            mid = (lo + hi) // 2
            
            if nums[mid] > nums[0]:
                lo = mid+1
            else:   # all elements distinct
                hi = mid
        
        rot_idx = lo
        
        def binarySearch(lo, hi):
            while lo <= hi:
                mid = (lo+hi) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if target<nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return -1
        
        n = len(nums)
        
        if n == 1:
            return 0 if nums[0] == target else -1
        
        if target == nums[rot_idx]:
            return rot_idx
        if target < nums[0]:
            return binarySearch(rot_idx, n-1)
        return binarySearch(0, rot_idx)