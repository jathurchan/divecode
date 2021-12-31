class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)

        answers = [0] * n

        stack = []

        for i in range(n-1):
            
            if temperatures[i] < temperatures[i+1]:
                answers[i] = 1
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answers[j] = i - j
            
            if temperatures[i] >= temperatures[i+1]:
                stack.append(i)
        

        while stack and temperatures[stack[-1]] < temperatures[n-1]:    # the last element has to be compared with other elements in the stack
                j = stack.pop()
                answers[j] = n-1 - j
        
        # do not care about the numbers that do not get values above them in the array because initialized with 0
        return answers
