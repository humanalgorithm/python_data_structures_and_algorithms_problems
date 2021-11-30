class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = set()
        self.permutations([], nums, len(nums), solutions, set())
        return solutions

    def permutations(self, pre, nums, num_length, solutions, visited):
        sorted_tuple = tuple(sorted(pre))
        if sorted_tuple in visited:
            return
        solutions.add(sorted_tuple)
        if len(pre) == num_length:
            return

        for x in range(0, len(nums)):
            num = nums[x]
            new_nums = nums[:x] + nums[x + 1:]
            self.permutations(pre + [num], new_nums, num_length, solutions, visited)

        visited.add(sorted_tuple)
