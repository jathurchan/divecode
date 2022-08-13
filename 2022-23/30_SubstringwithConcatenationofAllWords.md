# 30 Substring with Concatenation of All Words

## Description

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

**Example 1:**

> Input: s = "barfoothefoobarman", words = ["foo","bar"]

> Output: [0,9]

> Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.

> The output order does not matter, returning [9,0] is fine too.

**Example 2:**

> Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

> Output: []

**Example 3:**

> Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

> Output: [6,9,12]

**Constraints:**

- `1 <= s.length <= 104`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 30`
- `s` and `words[i]` consist of lowercase English letters.

## Solution

First, the concatenation is made of **every** word in `words`. Why do they precise that strings in `words` are of the same length? To quickly get the length of substring? It is obviously `num_of_words * length`.

My very first idea is to generate all concatenations possible from `words` by using each word (identified by their index in the array because a same string can be there more than once, `word` in example 2). And check for one of these concatenations every position possible (until `s.length - (num_of_words * length)`).

Actually there is better solution, I do not need to generate all combinaisons possible. I can just use a hashmap.

```python
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        freqOfWords = Counter(words)
        
        n = len(s)
        
        word_len = len(words[0])
        substr_size = word_len * len(words)
        
        result = []
        
        for i in range(n - substr_size + 1):
            
            temp_freq = freqOfWords.copy()
            num_of_words = 0
            
            for j in range(i, i+substr_size, word_len):
                if temp_freq[s[j:j+word_len]] > 0:
                    temp_freq[s[j:j+word_len]] -= 1
                    num_of_words += 1
                else:
                    break
            
            if num_of_words == len(words):
                result.append(i)
        
        return result
```

## Submission

Runtime: 1136 ms, faster than 43.03% of Python online submissions for Substring with Concatenation of All Words.

Memory Usage: 14.2 MB, less than 21.67% of Python online submissions for Substring with Concatenation of All Words.

