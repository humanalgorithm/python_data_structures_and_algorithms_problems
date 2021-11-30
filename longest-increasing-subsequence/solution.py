class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lis = [1] * (len(nums) + 1)

        for x in range(len(nums) - 1, -1, -1):
            for j in range(x, len(nums)):
                if nums[j] > nums[x]:
                    lis[x] = max(lis[x], 1 + lis[j])
        return max(lis)
