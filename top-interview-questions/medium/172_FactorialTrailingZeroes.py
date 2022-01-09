class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count_5 = 0
        count_2 = 0
        
        def countDiv(num, d):
            count = 0
            temp = num
            while temp % d == 0:
                temp //= d
                count += 1
            return count
        
        for k in range(2, n+1):
            count_5 += countDiv(k, 5)
            count_2 += countDiv(k, 2)
        
        return min(count_5, count_2)