class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1
    
    def isPowerOfFour2(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n & (n-1) != 0:  # n is not a power of 2
            return False
        
        power4Positions = 0b01010101010101010101010101010101    # 32 bits
        res = (power4Positions | n == power4Positions) # power of 4?
        return res