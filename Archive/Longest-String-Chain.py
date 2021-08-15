def longestStrChain(words):
    """
    1048. Longest String Chain

    Given a list of words, each word consists of English lowercase letters.
    Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in
    word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
    A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor
    of word_2, word_2 is a predecessor of word_3, and so on.
    Return the longest possible length of a word chain with words chosen from the given list of words.
    """

    def is_predecessor(word1, word2):   # is word1 a predecessor of word2
        n, p = len(word1), len(word2)
        
        if (n + 1) != p:    # compare lengths
            return False
        
        i,j = 0, 0

        extra_character_found = False

        while i < n and j < p and ((word1[i] == word2[j]) or not extra_character_found):
            if word1[i] != word2[j]:
                extra_character_found = True
                j += 1
            else:
                i += 1
                j += 1
        
        return i == n and (j == p or not extra_character_found)


    sorted_words = {}

    for word in words:
        
        l = len(word)
        
        if l in sorted_words:
            sorted_words[l].append(word)
        else:
            sorted_words[l] = [word]
    
    lengths = sorted(list(sorted_words.keys()))
    n_lengths = len(lengths)

    dp = [[1 for _ in range(len(sorted_words[l]))] for l in lengths]

    for prev_i in range(0,n_lengths-1):
        for nxt_i in range(1,n_lengths):
            
            prev_l, nxt_l = lengths[prev_i], lengths[nxt_i]

            prev = sorted_words[prev_l]
            nxt = sorted_words[nxt_l]

            m, n = len(prev), len(nxt)

            for i in range(m):
                for j in range(n):
                    
                    if is_predecessor(prev[i], nxt[j]):
                        
                        dp[nxt_i][j] = max(dp[nxt_i][j], 1 + dp[prev_i][i])
    
    longest_word_chain = 1

    for l in range(n_lengths):
        for elt in dp[l]:
            if elt > longest_word_chain:
                longest_word_chain = elt
    
    return longest_word_chain

print(longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
