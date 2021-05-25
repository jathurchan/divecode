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

        n = len(tokens)

        if n == 1:
            return int(tokens[0])

        ops = ['+', '-', '*', '/']

        def compute(l, r, o):
            if o == '+':
                return l + r
            elif o == '-':
                return l - r
            elif o == '*':
                return l * r
            else:
                return int(l / r)
        
        accu = []
        prev = []
        lft, rgt = 0, 0
        
        for i in range(n):
            if tokens[i] in ops:    # operator?

                op = tokens[i]

                if (tokens[i-1] not in ops) and (tokens[i-2] not in ops):
                    rgt = int(tokens[i-1])
                    lft = int(tokens[i-2])
                    accu.append(compute(lft, rgt, op))
                    if i > 2 and tokens[i-3] not in ops:
                        prev.append(i-3)
                elif (tokens[i-1] in ops):
                    rgt = accu.pop()
                    if prev:
                        pre = prev.pop()
                        lft = int(tokens[pre])
                        if pre > 0 and tokens[pre-1] not in ops:
                            prev.append(pre-1)
                    else:
                        lft = accu.pop()
                    accu.append(compute(lft, rgt, op))
                else:   # tokens[i-2] in ops and tokens[i-1] not in ops
                    lft = accu.pop()
                    rgt = int(tokens[i-1])
                    accu.append(compute(lft, rgt, op))

                print(i)
                print(accu)
                print(prev)

        
        return sum(accu)

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
                    




