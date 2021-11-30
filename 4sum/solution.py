class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        x, l, r = 0, 0, len(nums) - 1
        nums = sorted(nums)
        solutions = set()

        while len(nums) - x >= 4:
            first = nums[x]
            new_target = target - first
            new_array = nums[:x] + nums[x + 1:]
            l = 0
            while l < r:
                m = l + 1
                r = len(new_array) - 1
                while m < r:
                    curr = new_array[l] + new_array[m] + new_array[r]
                    if curr == new_target:
                        curr_tuple = tuple(sorted([first, new_array[l], new_array[m], new_array[r]]))
                        solutions.add(curr_tuple)
                        while m < r and new_array[m] == new_array[m + 1]:
                            m += 1
                        m += 1
                    elif curr < new_target:
                        m += 1
                    else:
                        r -= 1
                l += 1
            x += 1
        return list(solutions)