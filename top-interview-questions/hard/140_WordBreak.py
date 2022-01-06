class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        dictSet = set(wordDict)
        
        mem = defaultdict(list)
        
        def aux(s):
            
            if not s:
                return [[]]
            
            if s in mem:
                return mem[s]
            
            for endi in range(1, len(s)+1):
                word = s[:endi]
                if word in dictSet:
                    for subs in aux(s[endi:]):
                        mem[s].append([word]+subs)
            
            return mem[s]
        
        aux(s)
        
        return [" ".join(words) for words in mem[s]]