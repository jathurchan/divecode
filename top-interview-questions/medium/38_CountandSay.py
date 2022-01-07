class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        seq = "1"
        
        for _ in range(n-1):
            
            new_seq = ""
            
            i, n = 0, len(seq)
            
            while i < n:
                
                cnt = 1
                
                while i+cnt < n and seq[i] == seq[i+cnt]:
                    cnt += 1
                
                new_seq += str(cnt) + seq[i]
                
                i += cnt
            
            seq = new_seq
        
        return seq