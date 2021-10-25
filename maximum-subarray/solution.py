class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        working_sum = None
        for num in nums:
            max_sum = max(max_sum, working_sum)
            working_sum = working_sum + num if working_sum else num
            if num > working_sum:
                working_sum = num
        max_sum = max(max_sum, working_sum, nums[len(nums)-1])
        return max_sum

