class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        n = len(nums) - 1
        return [self.search(nums, n, target, 0, n + 1, True),
                self.search(nums, n, target, 0, n + 1, False)]

    def search(self, nums, n, target, start, end, left=True):
        pivot = (start + end) / 2
        if start > end or end < start or pivot > n or pivot < 0:
            return -1

        if nums[pivot] == target:
            if left and pivot > 0 and nums[pivot - 1] == target:
                return self.search(nums, n, target, start, pivot - 1, left)
            elif not left and pivot < n and nums[pivot + 1] == target:
                return self.search(nums, n, target, pivot + 1, end, left)
            return pivot
        elif nums[pivot] > target:
            return self.search(nums, n, target, start, pivot - 1, left)
        elif nums[pivot] < target:
            return self.search(nums, n, target, pivot + 1, end, left)
        return -1
