class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums) - 1
        self.quickSort(nums, l, r)

    def quickSort(self, nums, l, r):
        p = l
        if len(nums[l:r + 1]) <= 0:
            return
        pivot = nums[r]
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        self.quickSort(nums, l, p - 1)
        self.quickSort(nums, p + 1, r)
