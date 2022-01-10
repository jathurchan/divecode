class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        
        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # x + y
            
            while y > 0:
                temp = x^y
                y = (x&y) << 1
                x = temp
            
        else:
            # x - y
            
            while y > 0:
                temp = x^y
                y = ((~x)&y) << 1
                x = temp
            
        
        return x * sign