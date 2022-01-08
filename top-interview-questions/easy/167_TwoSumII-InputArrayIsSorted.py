class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(numbers)
        
        i, j = 0, n-1
        
        while numbers[i] + numbers[j] != target:
            
            if numbers[i] + numbers[j] < target:
                i += 1
                
            if numbers[i] + numbers[j] > target:
                j -= 1
        
        return [i+1, j+1]