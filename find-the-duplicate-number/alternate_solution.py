class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
            if num_count[num] > 1:
                return num
        return -1
