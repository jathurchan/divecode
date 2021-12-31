class Solution(object):
    def getBitMask(self, word):
        mask = 0
        for c in word:
            i = ord(c) - ord('a')
            mask |= 1 << i
        return mask

    def findNumOfValidWords(self, words, puzzles):
        letterFrequencies = {}
        for word in words:
            mask = self.getBitMask(word)
            letterFrequencies[mask] = letterFrequencies.get(mask, 0) + 1
        
        solution = [0] * len(puzzles)
        
        for i in range(len(puzzles)):
            puzzle = puzzles[i]
            mask = self.getBitMask(puzzle)
            subMask = mask
            total = 0
			
            firstBitIndex = ord(puzzle[0]) - ord('a')

            while True:
                if subMask >> firstBitIndex & 1:
                    total += letterFrequencies.get(subMask, 0)
                if subMask == 0:
                    break
                subMask = (subMask - 1) & mask
            solution[i] = total
        
        return solution