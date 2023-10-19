class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def decode(enS):
            stack = []
            for c in enS:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
                    
            return "".join(stack)

        return decode(s) == decode(t)