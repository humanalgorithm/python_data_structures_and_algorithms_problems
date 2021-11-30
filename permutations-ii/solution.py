class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = set()

        def searchPerm(pre, nums, visited):
            if tuple(pre) in visited:
                return
            visited.add(tuple(pre))
            if not nums:
                sol.add(tuple(pre))

            for x in range(0, len(nums)):
                searchPerm(pre + [nums[x]], nums[:x] + nums[x + 1:], visited)

        searchPerm([], nums, set())
        return sol