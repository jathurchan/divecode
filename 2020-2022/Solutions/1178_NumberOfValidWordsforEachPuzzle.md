# 1178. Number of Valid Words for Each Puzzle

## Description

With respect to a given `puzzle` string, a `word` is *valid* if both the following conditions are satisfied:

- `word` contains the first letter of `puzzle`.
- For each letter in `word`, that letter is in `puzzle`.
   - For example, if the puzzle is `"abcdefg"`, then valid words are `"faced"`, `"cabbage"`, and `"baggage"`, while
   - invalid words are `"beefed"` (does not include `'a'`) and `"based"` (includes `'s'`which is not in the puzzle).

Return *an array* `answer`*, where* `answer[i]` *is the number of words in the given word list* `words`*that is valid with respect to the puzzle* `puzzles[i]`.

**Example 1:**

**Input:** words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

**Output:** [1,1,3,2,4,0]

**Explanation:**

1 valid word for "aboveyz" : "aaaa"

1 valid word for "abrodyz" : "aaaa"

3 valid words for "abslute" : "aaaa", "asas", "able"

2 valid words for "absoryz" : "aaaa", "asas"

4 valid words for "actresz" : "aaaa", "asas", "actt", "access"

There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.

**Example 2:**

**Input:** words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]

**Output:** [0,1,3,2,0]

**Constraints:**

- `1 <= words.length <= 105`
- `4 <= words[i].length <= 50`
- `1 <= puzzles.length <= 104`
- `puzzles[i].length == 7`
- `words[i]` and `puzzles[i]` consist of lowercase English letters.
- Each `puzzles[i]` does not contain repeated characters.

## Thoughts

- Rather than using a 26-boolean array to memorize the letters that appear in the word, we use **bitmasking**.
- The length of puzzles is equal to 7. By comparing the bitmaps of words and the subsets of the bitmap of the puzzle, we can quickly get the words that satisfy the 2nd condition.
- **First**, iterate over words and compute all bitmasks. Store them in a hasmap with frequency.
- **Second**, iterate over puzzles, compute their bitmaps. And, check if any of its subset (**submask**) is present in the hash map.
- **Third**, only consider submasks having a set bit corresponding to the first character of the puzzle.

## Solution

```python
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
```

