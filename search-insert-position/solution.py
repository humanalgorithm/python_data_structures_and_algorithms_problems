import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target > nums[-1]:
            return len(nums)

        return bisect.bisect_left(nums, target)
