def minimumLength(s):
    """
        1750. Minimum Length of String After Deleting Similar Ends

        Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply
        the following algorithm on the string any number of times:
        Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
        Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
        The prefix and the suffix should not intersect at any index.
        The characters from the prefix and suffix must be the same.
        Delete both the prefix and the suffix.
        Return the minimum length of s after performing the above operation any number of times (possibly zero times).
    """

    n = len(s)

    if n == 0:  # empty string
        return 0
    elif n == 1:    # only one character
        return 1
    
    i, j = 0, n-1
    fst_i, fst_j = i, j

    while i < j:    # no intersection between prefix and suffix + prefix and suffix exist ?
        if s[i+1] == s[i]:  # prefix
            i += 1
        if s[j-1] == s[j]:  # suffix
            j -= 1
        
        if s[i+1] != s[i] and s[j-1] != s[j]:   # prefix and suffix already found
            if s[i] == s[j]:    # characters from prefix and suffix same ?
                i += 1
                j -= 1
                fst_i, fst_j = i, j
            else:
                return fst_j - fst_i + 1

    if i == j and not ( (i-1 >= 0 and s[i] == s[i-1]) or (j+1 < n and s[j] == s[j+1])):  # only one character different from characters of prexix / suffix
        return 1
    else:   # (i > j) : empty string or last character should be with prefix / suffix
        return 0