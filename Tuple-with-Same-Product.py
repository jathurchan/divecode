def tupleSameProduct(nums):
    """
        1726. Tuple with Same Product

        Given an array nums of distinct positive integers,
        return the number of tuples (a, b, c, d) such that a * b = c * d
        where a, b, c, and d are elements of nums, and a != b != c != d.
    """
    
    n = len(nums)
    res = 0
    products_with_freq = {}
    for i in range(n):
        for j in range(i+1, n):
            product = nums[i] * nums[j]
            if product in products_with_freq:
                res += products_with_freq[product]
                products_with_freq[product] += 1
            else:
                products_with_freq[product] = 1
    return 8 * res
            