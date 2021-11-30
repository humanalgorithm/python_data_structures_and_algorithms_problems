class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.count_dict = set()
        [self.count_dict.add(num) for num in nums]

        total_count = 0
        for key in self.count_dict:
            total_count = max(total_count, self.get_consecutive(key))
        return total_count

    def get_consecutive(self, key):
        if key - 1 in self.count_dict:
            return 0
        count_line = 0
        iter_key = key
        while iter_key in self.count_dict:
            iter_key += 1
            count_line += 1
        return count_line
