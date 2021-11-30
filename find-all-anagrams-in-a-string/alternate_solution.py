import string

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict
        if len(s) == 0 or len(p) > len(s):
            return []

        p_count = defaultdict(int)

        for char in string.ascii_lowercase:
            p_count[char] = 0
        for letter in p:
            p_count[letter] += 1

        s_count = defaultdict(int)
        for char in string.ascii_lowercase:
            s_count[char] = 0
        for x in range(0, len(p) - 1):
            s_count[s[x]] += 1

        start, output = 0, []

        while start + len(p) - 1 < len(s):
            letter = s[start + len(p) - 1]
            s_count[letter] += 1
            if s_count == p_count:
                output.append(start)
            s_count[s[start]] -= 1
            start += 1
        return output
