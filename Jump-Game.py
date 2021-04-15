def canJump(nums):
    """
    55. Jump Game

    Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.
    """

    n = len(nums)

    ind_to_visit = [0]
    visted_indices = set()

    while ind_to_visit:
        curr_i = ind_to_visit.pop()
        visted_indices.add(curr_i)

        if curr_i == n-1:   # last index ?
            return True
        
        max_jump_len = nums[curr_i]

        for k in range(1, max_jump_len+1):
            next_i = curr_i + k
            if next_i < n and next_i not in visted_indices:
                ind_to_visit.append(next_i)
    
    return False

# print(canJump([3,2,1,0,4]))
