class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        solutions, candidates = [], sorted(candidates)
        self.search(candidates, 0, target, [], solutions)
        return solutions

    def search(self, candidates, i, target, nums, solutions):
        if i == len(candidates):
            return
        if candidates[i] + sum(nums) == target:
            solutions.append(nums + [candidates[i]])
            return
        if sum(nums) + candidates[i] > target:
            return

        self.search(candidates, i, target, nums + [candidates[i]], solutions)
        self.search(candidates, i + 1, target, nums, solutions)
