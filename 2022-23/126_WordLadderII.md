# 126 Word Ladder II

## Description

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k is in wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the shortest transformation sequences from* `beginWord` *to* `endWord`*, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words* `[beginWord, s1, s2, ..., sk]`.

**Example 1:**

> **Input**: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

> **Output**: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

> **Explanation**: There are 2 shortest transformation sequences:

> "hit" -> "hot" -> "dot" -> "dog" -> "cog"

> "hit" -> "hot" -> "lot" -> "log" -> "cog"

**Example 2:**

> **Input**: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]

> **Output**: []

> **Explanation**: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

**Constraints:**

- `1 <= beginWord.length <= 5`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 500`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are unique.

## Solution

First, check whether endWord is in wordList. If it is not the case, the answer is immediately `[]`.

Store wordList as a set.

BFS (Breadth First Search): Given the beginWord, iterate over each character of beginWord and replace it by an another character from a to z.

- If the newly created word is the endWord add it to the answer list and ignore this path.
- If not,
   - Check whether this word is in the set containing all words already appeared in this path. If that is the case, just ignore this path (loop).
   - Check whether this word is in the set containing all words of wordList. If it is there, then continue: redo everything from the next word with the updated set (containing all appeared words in the path) → recursive function
   - If the word is not in wordList, just ignore this path.

```python
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        n = len(beginWord)
        
        wordList = set(wordList)
        
        answer = []
        
        def explore(currWord, prevPath):
            
            for i in range(n):
                for k in range(26):
                    c = chr(ord('a') + k)
                    
                    newWord = currWord[:i] + c + currWord[i+1:]
                    
                    if newWord in wordList:    # a word in wordList
                    
                        if newWord == endWord:
                            answer.append(prevPath + [newWord])
                        
                        elif newWord not in prevPath:    # not already appeared    
                            explore(newWord, prevPath + [newWord])
        
        explore(beginWord, [beginWord])  # populate answer
        
        if answer == []:
            return []
        
        minLength = min([len(l) for l in answer])   # Get minimum length
        
        final = []
        
        for l in answer:
            if len(l) == minLength:
                final.append(l)
        
        return final
```

## Submission

Time Limit Exceeded

19 / 35 test cases passed

Last executed input

```python
"qa"
"sq"
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
```

