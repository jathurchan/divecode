class Solution(object):
    """
        150. Evaluate Reverse Polish Notation

            Evaluate the value of an arithmetic expression in Reverse Polish Notation.
            Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
            Note that division between two integers should truncate toward zero.
            It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result,
            and there will not be any division by zero operation.

            Constraints:
                -   1 <= tokens.length <= 104
                -   tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
    """

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        ops = ["+", "-", "*", "/"]

        for elt in tokens:
            if elt not in ops:
                stack.append(int(elt))
            else:
                rgt, lft = stack.pop(), stack.pop()
                if elt == "+":
                    stack.append(rgt+lft)
                elif elt == "-":
                    stack.append(lft-rgt)
                elif elt == "*":
                    stack.append(lft*rgt)
                else:
                    stack.append(int(float(lft)/rgt))
        return stack.pop()

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
                    




