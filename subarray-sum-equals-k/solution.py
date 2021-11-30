class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        sol_count, sum_num = 0, 0
        sum_map = defaultdict(int)
        sum_map[0] = 1

        for x in range(0, len(nums)):
            sum_num += nums[x]
            if sum_map.get(sum_num - k) is not None:
                sol_count += sum_map.get(sum_num - k)
            sum_map[sum_num] += 1
        return sol_count
