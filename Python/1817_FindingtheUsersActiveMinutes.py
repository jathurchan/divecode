class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        idx, n = 0, len(logs)
        
        logs.sort(key=lambda log: log[0])   # sort by users
        
        answer = [0] * k
        
        while idx < n:
            
            counter = 1
            mins = set([logs[idx][1]])
            
            while idx+counter<n and logs[idx][0] == logs[idx+counter][0]:
                mins.add(logs[idx+counter][1])
                counter += 1
            
            uam = len(mins)
            
            answer[uam-1] += 1
            
            idx += counter
        
        return answer