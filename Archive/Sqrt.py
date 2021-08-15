def mySqrt(x):
    """
    69. Sqrt(x)

    Given a non-negative integer x, compute and return the square root of x.
    Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
    """

    i = 1

    while i*i < x:
        i += 1
    
    if i*i == x:
        return i
    else:
        return i-1