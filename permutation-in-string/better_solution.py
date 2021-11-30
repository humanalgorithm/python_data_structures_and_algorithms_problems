class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import defaultdict
        s1_count, s2_count = defaultdict(int), defaultdict(int)

        for char in string.ascii_lowercase:
            s1_count[char] = 0
            s2_count[char] = 0
        for char in s1:
            s1_count[char] += 1

        start, window = 0, len(s1)

        for x in range(0, min(len(s1), len(s2))):
            s2_count[s2[x]] += 1
        while start + window <= len(s2):
            if start != 0:
                new_char = s2[start + window - 1]
                s2_count[new_char] += 1
            if s2_count == s1_count:
                return True
            remove_char = s2[start]
            s2_count[remove_char] -= 1
            start += 1
        return False
