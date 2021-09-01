def findLUSIl(a, b):
    """
    522. Longest Uncommon Subsequence II
    """
    if a == b:
        return -1
    elif len(a) == len(b):
        return len(a)
    else:   # len(a) != len(b)
        return max(len(a), len(b))
