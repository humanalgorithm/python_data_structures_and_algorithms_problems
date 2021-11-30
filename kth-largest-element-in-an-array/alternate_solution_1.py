class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort(reverse=True)
        # return nums[k-1]
        counter = 0
        original_len = len(nums)
        while nums:
            max_index = -1
            import sys
            if len(nums) + k == original_len:
                break
            max_num = -sys.maxint
            for x in range(0, len(nums)):
                max_num = max(max_num, nums[x])
                if max_num == nums[x]:
                    max_index = x
            nums.pop(max_index)
        return max_num
