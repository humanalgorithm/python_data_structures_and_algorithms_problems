class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        num_copy = [item for item in nums]
        counter = 0
        stack = []
        while counter < k:
            pos = (len(nums) - counter) % len(nums) - 1
            stack.append(nums[pos])
            counter += 1

        counter = 0
        stack_len = len(stack)
        while stack and counter < len(nums):
            nums[counter] = stack.pop()
            counter += 1

        remaining = len(nums) - stack_len
        for x in range(stack_len, stack_len + remaining):
            nums[x] = num_copy[x - stack_len]
