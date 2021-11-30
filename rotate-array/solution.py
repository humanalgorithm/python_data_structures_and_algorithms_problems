class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_insert = [0 for item in range(0, k)]
        num_copy = num_insert + nums

        p1 = len(num_copy) - 1
        p2 = len(num_copy) - 1 - len(nums)

        while p1 >= 0:
            num_copy[p2], num_copy[p1] = num_copy[p1], num_copy[p2]
            p1 -= 1
            p2 -= 1

        for x in range(0, len(nums)):
            nums[x] = num_copy[len(num_copy) - len(nums) + x]