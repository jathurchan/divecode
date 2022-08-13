class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        visited = [False] * n

        maxCycLen = 1

        for curr in range(n):
            if not visited[curr]:  # Visiting the number for the first time
                
                visited[curr] = True
                cycLen = 1
                i = nums[curr]

                while i != curr:
                    cycLen += 1
                    visited[i] = True
                    i = nums[i]     # Update i
                
                if cycLen > maxCycLen:
                    maxCycLen = cycLen
        return maxCycLen

solution = Solution()
print(solution.arrayNesting([0,1,2]))



