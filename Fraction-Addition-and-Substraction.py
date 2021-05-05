class Solution(object):
    """
    Given a string expression representing an expression of fraction addition and
    subtraction, return the calculation result in string format.
    The final result should be an irreducible fraction. If your final result is an integer,
    say 2, you need to change it to the format of a fraction that has a denominator 1.
    So in this case, 2 should be converted to 2/1.

    Constraints:
        -   The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
        -   Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
        -   The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
        -   The number of given fractions will be in the range [1, 10].
        -   The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
    """

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        n = len(expression)

        # Get fractions
        fractions = []
        common_den = 1

        for i in range(n):
            if expression[i] == '/':

                l, r = i, i

                while l > 0 and expression[l] not in ['+', '-']:
                    l -= 1
                
                while r < n and expression[r] not in ['+', '-']:
                    r += 1
                
                num, den = int(expression[l:i]), int(expression[i+1:r])
                fractions.append((num, den))
                common_den *= den
                
        # Add fractions
        common_num = 0
        for num, den in fractions:
            common_num += num * (common_den // den)


        # Get an irreductible fraction
        d = self.compute_gcd(common_num, common_den)

        common_num //= d
        common_den //= d

        # Return the result
        return str(common_num) + "/" + str(common_den)
    
    def compute_gcd(self, a, b):
        while b:
            a, b = b, a % b
        
        return a

sol = Solution()
print(sol.fractionAddition("-1/2+1/2"))