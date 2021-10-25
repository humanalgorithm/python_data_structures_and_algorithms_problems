class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def findPermutations(prefix, postfix):
            if len(prefix) + len(postfix) == n:
                combinations.add(tuple(prefix + postfix))
            for i in range(0, len(postfix)):
                findPermutations(prefix + [postfix[i]], postfix[0:i] + postfix[i + 1:])

        n = len(nums)
        combinations = set()
        findPermutations([], nums)
        return list(combinations)
