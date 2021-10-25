class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = {0: 1}
        r = {len(nums) - 1: 1}

        # l[0] = 1
        # l[1] = 4 * 1
        # l[2]  = 4 * 5

        for x in range(1, len(nums)):
            num = nums[x - 1] * l[x - 1]
            l[x] = num

        # print l

        for x in range(len(nums) - 2, -1, -1):
            num = nums[x + 1] * r[x + 1]
            r[x] = num

        # print r

        num_output = []
        for x in range(0, len(nums)):
            num_output.append(l[x] * r[x])
        return num_output
