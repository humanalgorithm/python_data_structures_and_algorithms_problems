from itertools import chain


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def searchCombinations(target, path):
            if target < 0:
                return False
            if target == 0:
                path = tuple(sorted(path))
                result.add(path)
                return
            for x in range(0, n):
                if candidates[x] > target:
                    break
                searchCombinations(target - candidates[x], path + [candidates[x]])

        result = set()
        n = len(candidates)
        candidates.sort()
        searchCombinations(target, [])
        return list(result)

