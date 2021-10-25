class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        zero_count = nums.count(0)
        for x in range(0, zero_count):
            nums.remove(0)
            nums.append(0)
        return nums
        """

        x, count = 0, 0
        while x < len(nums) and count < len(nums):
            if nums[x] == 0:
                nums.append(0)
                nums.pop(x)
                x -= 1
            x += 1
            count += 1
        return nums
