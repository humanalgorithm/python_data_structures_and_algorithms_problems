class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right - left) / 2
            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle

        pivot = left
        left = 0
        right = len(nums) - 1
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot

        while left <= right:
            middle = left + (right - left) / 2
            if nums[middle] == target:
                return middle
            if left == right:
                break
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1