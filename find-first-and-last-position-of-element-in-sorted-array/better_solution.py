class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.searchLow(nums, target),
                self.searchHigh(nums, target)]

    def searchLow(self, nums, target):
        index, left, right = -1, 0, len(nums) - 1

        while left <= right:
            midpoint = left + (right - left) / 2
            if nums[midpoint] >= target:
                right = midpoint - 1
            elif nums[midpoint] <= target:
                left = midpoint + 1

            index = midpoint if nums[midpoint] == target else index
        return index

    def searchHigh(self, nums, target):
        index, left, right = -1, 0, len(nums) - 1

        while left <= right:
            midpoint = left + (right - left) / 2

            if nums[midpoint] <= target:
                left = midpoint + 1
            elif nums[midpoint] >= target:
                right = midpoint - 1
            index = midpoint if nums[midpoint] == target else index
        return index
