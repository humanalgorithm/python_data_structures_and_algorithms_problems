class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        nums_dict = defaultdict(int)

        for num in nums:
            nums_dict[num] += 1

        num_tuples = [(key, value) for key, value in nums_dict.items()]
        sorted_tuple = sorted(num_tuples, key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_tuple[:k]]
