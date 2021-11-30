class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                i+=1
                continue
            j = i+1
            while j < len(nums):
                if nums[i] == 0 and nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                j+=1
            i+=1
    