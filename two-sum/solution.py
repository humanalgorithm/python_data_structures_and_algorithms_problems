class Solution(object):

    def twoSum(self, nums, target):
        nums_dict = {}
        for index, num in enumerate(nums):
            computed = target - num
            if nums_dict.get(computed) is not None:
                return [nums_dict.get(computed), index]
            nums_dict[num] = index