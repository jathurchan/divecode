class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def getNumOf1s(num):
            ans = 0
            while num > 0:
                ans += num & 1
                num >>= 1
            return ans
        
        numOf1sMap = {}
        for num in arr:
            numOf1sMap[num] = getNumOf1s(num)

        return sorted(arr, key=lambda num: (numOf1sMap[num], num))