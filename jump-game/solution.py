class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        last_reachable = len(nums) - 1
        for x in range(len(nums) - 1, -1, -1):
            jump = nums[x]
            if x + jump >= last_reachable:
                last_reachable = x

        return True if last_reachable == 0 else False
