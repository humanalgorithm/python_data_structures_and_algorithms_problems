class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    l += 1
                    r -= 1
        return -1
