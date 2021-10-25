class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        nums_set = []
        i, len_r = 0, len(nums) - 1
        while i < len(nums) and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            l = i + 1
            r = len_r
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    nums_set.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                total = nums[i] + nums[l] + nums[r]
                if total <= 0:
                    l += 1
                else:
                    r -= 1
            i += 1
        return nums_set
