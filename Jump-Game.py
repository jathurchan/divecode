def canJump(nums):
    """
    55. Jump Game

    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    """

    n = len(nums)

    mem = [-1] * n  # -1 : unknown position, 0 : bad position and 1 : good position (can reach the last index from)
    mem[n-1] = 1     # last index is obviously a good position.

    for i in range(n-1):

        curr_i = n - 2 - i  # start from the right side
        max_jump_len = nums[curr_i]

        for k in range(1, max_jump_len + 1):

            next_i = curr_i + k
            if next_i < n and mem[next_i] == 1:
                mem[curr_i] = 1
                break
        
        if mem[curr_i] == -1:
            mem[curr_i] = 0

    return mem[0] == 1
