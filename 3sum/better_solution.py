class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, solution_set = sorted(nums), set()
        left, right = 0, len(nums)-1

        while left < len(nums):
            mid = left + 1
            right = len(nums)-1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0:
                    solution = sorted([nums[left], nums[mid], nums[right]])
                    solution_set.add(tuple(solution))
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid +=1
                    while right > mid and nums[right] == nums[right-1]:
                        right -=1
                    mid +=1
                elif total > 0:
                    right -=1
                elif total < 0:
                    mid +=1
            left +=1
        return solution_set
