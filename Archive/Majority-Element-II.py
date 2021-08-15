def majorityElement(nums):
    """
    229. Majority Element II

    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
    """

    n = len(nums)

    freq = {}
    order = []

    for elt in nums:
        if elt in freq:
            freq[elt] += 1
        else:
            freq[elt] = 1
            order.append(elt)
    
    res = []
    for elt in order:
        if freq[elt] > (n // 3):
            res.append(elt)
    return res

        
