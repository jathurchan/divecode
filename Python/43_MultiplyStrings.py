class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if num1 == "0" or num2 == "0":  # Product by 0?
            return "0"

        n1, n2 = len(num1), len(num2)

        res_arr = [0]*(n1+n2)   # array of length n1+n2+1

        for i1 in range(n1-1, -1, -1):
            for i2 in range(n2-1, -1, -1):
                res_arr[i1+i2+1] += int(num1[i1]) * int(num2[i2])  # multiply digit by digit
                res_arr[i1+i2] += res_arr[i1+i2+1] // 10
                res_arr[i1+i2+1] %= 10

        res = ""
        for d in res_arr:
            res += str(d)
        
        i=0
        while i < len(res) and res[i] == "0":   # Eliminate zeroes at the beginning
            i += 1
        
        return res[i:]