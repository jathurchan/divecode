class Solution(object):
    """
    84. Largest Rectangle in Histogram

    Given an array of integers heights representing the histogram's bar height where the width
    of each bar is 1, return the area of the largest rectangle in the histogram.

    Constraints:

        -   1 <= heights.length <= 105
        -   0 <= heights[i] <= 104
    """

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        n = len(heights)

        max_area = 0

        for i in range(n):
            curr_height = heights[i]
            r_cnt, l_cnt = 1, 1

            while i + r_cnt < n and heights[i+r_cnt] >= curr_height:
                r_cnt += 1
            
            while i - l_cnt >= 0 and heights[i-l_cnt] >= curr_height:
                l_cnt += 1
            
            area = (r_cnt + l_cnt - 1) * curr_height
            if area > max_area:
                max_area = area
        
        return max_area

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
print(sol.largestRectangleArea([2,1,2]))
            
