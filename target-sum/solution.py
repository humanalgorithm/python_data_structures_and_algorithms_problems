class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def backtrack(i, total, track):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in track:
                return track[(i, total)]

            track[(i, total)] = (backtrack(i + 1, total + nums[i], track) +
                                 backtrack(i + 1, total - nums[i], track))
            return track[(i, total)]

        return backtrack(0, 0, dict())
