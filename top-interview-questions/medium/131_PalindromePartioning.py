class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        
        def isPalindrome(ss):
            for i in range(len(ss)//2):
                if ss[i] != ss[len(ss)-1-i]:
                    return False
            return True
        
        def build(i, acc):
            if i == len(s):
                ans.append(acc)
            
            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    build(j, acc + [s[i:j]])
        
        build(0, [])
        return ans