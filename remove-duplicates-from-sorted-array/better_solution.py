class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pop_indexes, total_popped = [], 0

        for x in range(0, len(nums) - 1):
            if nums[x] == nums[x + 1]:
                pop_indexes.append(x)

        for pop_index in pop_indexes:
            nums.pop(pop_index - total_popped)
            total_popped += 1
        return len(nums)
