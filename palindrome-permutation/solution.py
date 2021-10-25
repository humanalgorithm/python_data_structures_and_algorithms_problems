class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_dict = {}
        for char in s:
            if not char_dict.get(char):
                char_dict[char] = 0
            char_dict[char] += 1

        evens_count = [value % 2 == 0 for key, value in char_dict.iteritems()].count(True)
        odds_count = len(char_dict.keys()) - evens_count
        return True if odds_count == 1 or odds_count == 0 else False
