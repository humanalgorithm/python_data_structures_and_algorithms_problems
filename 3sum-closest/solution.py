class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        nums = sorted(nums)
        closest_num = (sys.maxint, sys.maxint)
        l = 0

        while l < len(nums) - 2:
            m = l + 1
            r = len(nums) - 1

            while m < r:
                curr = nums[l] + nums[m] + nums[r]
                diff = abs(target - curr)
                min_diff = min(closest_num[0], diff)
                if min_diff == diff:
                    closest_num = (diff, curr)

                if curr == target:
                    return curr
                elif curr < target:
                    while m < r and nums[m] == nums[m + 1]:
                        m += 1
                    m += 1
                else:
                    while r > m and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
            l += 1
        return closest_num[1]
