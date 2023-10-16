class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [math.comb(rowIndex, colIndex) for colIndex in range(0, rowIndex+1)]