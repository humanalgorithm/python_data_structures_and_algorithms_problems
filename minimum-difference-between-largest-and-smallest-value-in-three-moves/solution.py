class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums) <=3:
            return 0
        sol1 = nums[-4] - nums[0]
        sol2 = nums[-3] - nums[1]
        sol3 = nums[-2] - nums[2]
        sol4 = nums[-1] - nums[3]
        return min(sol1, sol2, sol3, sol4)
