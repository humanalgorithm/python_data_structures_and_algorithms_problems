class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        solutions = []
        candidates.sort()

        def searchCandidates(current, pos, target):
            if target == 0:
                solutions.append(current)
                return
            if target < 0:
                return

            prev = -1
            for x in range(pos, len(candidates)):
                num = candidates[x]
                if num == prev:
                    continue
                curr_copy = current + [num]
                searchCandidates(curr_copy, x + 1, target - num)
                prev = num

        searchCandidates([], 0, target)
        return solutions
