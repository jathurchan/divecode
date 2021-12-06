class Solution:
    def minCostToMoveChips(self, position):
        a, b = 0, 0
        for p in position:
            if p % 2 == 0:
                a += 1
            else:
                b += 1
        return min(a, b)