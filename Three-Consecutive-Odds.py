def threeConsecutiveOdds(arr):
    """
    1550. Three Consecutive Odds

    Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
    """

    n = len(arr)

    for i in range(n-2):
        counter = 0
        while counter < 3 and arr[i+counter] % 2 == 1:
            counter += 1
        if counter == 3:
            return True
    
    return False