def mostCommonWord(paragraph, banned):
    """
    819. Most Common Word

    Given a string paragraph and a string array of the banned words banned, return the most frequent
    word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
    The words in paragraph are case-insensitive and the answer should be returned in lowercase.
    """

    words_in_paragraph = {}
    banned_words = set(banned)
    
    symbols = set(["!", "?", "'", ",", ";", "."])

    def add_word(word):
        if len(word) < 1:
            return

        word = word.lower()

        if word not in words_in_paragraph:
            words_in_paragraph[word] = 1
        else:
            words_in_paragraph[word] += 1

    for word in paragraph.split(" "):
        if len(word) >= 1 and word[-1] in symbols:
            word = word[:-1]
        
        word_divided = False

        for symbol in symbols:
            if symbol in word:
                word_divided = True
                word = word.replace(symbol, ' ')
            
        if word_divided:
            sub_words = word.split(" ")

            for sub_word in sub_words:
                add_word(sub_word)
        else:
            add_word(word)

    max_freq = 0
    most_freq_word = ""

    for word, freq in words_in_paragraph.items():
        if word not in banned_words:
            if freq > max_freq:
                max_freq = freq
                most_freq_word = word
    
    return most_freq_word

    
print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. Bob hit a ball, the hit BALL flew far after it was hit. "
,["hit"]))