class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        while counter < len(nums):
            if nums[counter] == val:
                del nums[counter]
                counter -=1
            counter +=1
        return len(nums)
