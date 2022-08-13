class Solution(object):
    """
        658. Find K Closest Elements

        Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
        The result should also be sorted in ascending order.

        An integer a is closer to x than an integer b if:
            -   |a - x| < |b - x|, or
            -   |a - x| == |b - x| and a < b

        Constraints:
            -   1 <= k <= arr.length
            -   1 <= arr.length <= 104
            -   arr is sorted in ascending order.
            -   -104 <= arr[i], x <= 104
    """

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        def compute(a):
            return abs(x-a)
        
        s_arr = sorted(arr, key=compute)

        i = 0
        n = len(arr)

        while i < n:
            counter = 1
            while i + counter < n and compute(s_arr[i]) == compute(s_arr[i+counter]):
                counter += 1

            if counter > 1:
                s_arr[i:i+counter] = sorted(s_arr[i:i+counter])
            
            i += counter

        return sorted(s_arr[:k])

sol = Solution()
print(sol.findClosestElements([1,2,3,4,5], 4, 3))

        