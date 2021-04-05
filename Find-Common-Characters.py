

def commonChars(A):
    """
        1002. Find Common Characters

        Given an array A of strings made only from lowercase letters, return a list
        of all characters that show up in all strings within the list (including duplicates).
        For example, if a character occurs 3 times in all strings but not 4 times, you need to
        include that character three times in the final answer.
        You may return the answer in any order.
    """

    c_in_all_strings = {}

    for c in A[0]:     # init c_in_all_strings
        if c not in c_in_all_strings:
            c_in_all_strings[c] = 1
        else:
            c_in_all_strings[c] += 1

    for s in A[1:]:
        
        characters = {}

        for c in s:
            if c not in characters:
                characters[c] = 1
            else:
                characters[c] += 1
        
        keys_s = set(characters.keys())
        keys_all_s = set(c_in_all_strings.keys())

        keys = keys_s & keys_all_s  # characters that appear in both dictionaries


        for k in (keys_all_s - keys):   # delete characters
            del c_in_all_strings[k]
        
        for k in keys:  # update number of occurences
            c_in_all_strings[k] = min(c_in_all_strings[k], characters[k])

    
    res = []

    for c, n_of_occ in c_in_all_strings.items():
        res += ([c] * n_of_occ)
    
    return res
