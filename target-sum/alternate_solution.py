class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from collections import defaultdict
        nums_dict = defaultdict(dict)

        first_num = nums[0]
        if first_num == 0:
            nums_dict[0][first_num] = 2
        else:
            nums_dict[0][first_num] = 1
            nums_dict[0][-1 * first_num] = 1

        for x in range(1, len(nums)):
            nums_dict[x] = defaultdict(int)
            for num, count in nums_dict[x - 1].items():
                nums_dict[x][num + nums[x]] += count
                nums_dict[x][num - nums[x]] += count
        return nums_dict[len(nums) - 1].get(target, 0)
    