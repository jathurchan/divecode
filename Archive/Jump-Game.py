def canJump(nums):
    """
    55. Jump Game

    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    """

    n = len(nums)

    last_i = n - 1  # last index

    for curr_i in range(n-2, -1, -1):
        if (curr_i + nums[curr_i] >= last_i):
            last_i = curr_i
    
    return last_i == 0
