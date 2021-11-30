class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums_copy = [0] * len(nums)

        for x in range(0, len(nums)):
            elem = nums[x]
            new_index = (x + k) % len(nums)
            nums_copy[new_index] = elem

        for x in range(0, len(nums_copy)):
            nums[x] = nums_copy[x]