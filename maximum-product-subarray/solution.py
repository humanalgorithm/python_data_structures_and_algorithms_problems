class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: Lst[int]
        :rtype: int
        """
        min_num, max_num = 1, 1
        result = max(nums)

        for num in nums:
            if num == 0:
                min_num = 1
                max_num = 1
                continue
            temp = min_num
            min_num = min(min_num * num, max_num * num, num)
            max_num = max(max_num * num, temp * num, num)

            result = max(result, min_num, max_num)
        return result