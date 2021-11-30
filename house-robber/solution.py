class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0, 0] + nums
        for x in range(2, len(nums)):
            nums[x] = max(nums[x] + nums[x-2], nums[x-1])
        return nums[-1]
