class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)

        def dfs(i, sum_path, sum_nums, visited):
            if sum_nums in visited:
                return False
            visited.add(sum_nums)

            if sum_path > sum_nums:
                return False

            if (sum_path and sum_nums) and sum_path == sum_nums:
                return True

            for x in range(i, len(nums)):
                result = dfs(x + 1, sum_path + nums[x], sum_nums - nums[x], visited)
                if result:
                    return True

        return dfs(0, 0, sum(nums), set())