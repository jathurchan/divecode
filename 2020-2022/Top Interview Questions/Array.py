class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # using two pointers
        # i for the current element we read in nums
        # j for the next index of expectedNums that is going to store the next element

        n = len(nums)

        i, j = 0, 0

        while i < n:

            nums[j] = nums[i]
            j += 1
            
            # next index to explore ignoring all duplicates
            cnt = 1
            while (i+cnt < n) and (nums[i] == nums[i+cnt]):
                cnt += 1
            
            i += cnt
        
        return j
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)

        if n < 2:
            return 0    # No profit
        
        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:     # we can buy and sell on the same day
                profit += (prices[i] - prices[i-1])
        
        return profit

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Rotate k times

        # n = len(nums)

        # u, v = 0, 0

        # for j in range(k):
        #     fst = nums[0]
        #     u = fst
        #     for i in range(n-1):
        #         v = nums[i+1]
        #         nums[i+1] = u
        #         u = v
        #     nums[0] = u
        # return nums

        # Reversing

        # n = len(nums)

        # k = k % n

        # return list(reversed(list(reversed(nums[:n-k])) + list(reversed(nums[n-k:]))))

        # Slicing

        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums = sorted(nums)

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False
                
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Using xor ( a^a^b = b)

        singOne = nums[0]
        for num in nums[1:]:
            singOne ^= num
        return singOne
    
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = {}

        for num in nums1:   # store all numbers that appear in nums1 (with the number of occurences)
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        intersection = []

        for num in nums2:   # build intersection while going through the numbers in nums2
            if num in freq and freq[num] > 0:
                freq[num] -= 1
                intersection.append(num)
        
        return intersection

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits)-1

        while i>=0 and (digits[i]+1 == 10):
            digits[i] = 0
            i -= 1

        if i == -1:     # when you have to add a 1 (no leading zeroes)
            return [1] + digits

        digits[i] += 1

        return digits

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Using 2 pointers (1 to fill the element *i* and an another to explore *j*)

        i, j = 0, 0     # i <= j

        while (j < len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        while i < len(nums):
            nums[i] = 0
            i += 1
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hash:
                return [i, hash[diff]]
            
            hash[nums[i]] = i
        
        return []
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):  # rows
            nums = set()
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num in nums:
                        return False
                    else:
                        nums.add(num)
        
        for j in range(9):  # cols
            nums = set()
            for i in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num in nums:
                        return False
                    else:
                        nums.add(num)
        
        for k in range(3):
            for l in range(3):
                nums = set()
                for i in range(3*k, 3*(k+1)):
                    for j in range(3*l, 3*(l+1)):
                        if board[i][j] != ".":
                            num = int(board[i][j])
                            if num in nums:
                                return False
                            else:
                                nums.add(num)

        return True

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # vertical symmetry
        for i in range(n//2):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][j]
                matrix[n-1-i][j] = temp

        # diagonal symmetry
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
