class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        i, j = 0, len(heights) - 1
        while not i >= j:
            if heights[i] <= heights[j]:
                area = (j - i) * heights[i]
                i += 1
            else:
                area = (j - i) * heights[j]
                j -= 1
            max_area = max(max_area, area)
        return max_area

