class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import defaultdict
        char_dict = defaultdict(int)

        for char in s:
            char_dict[char] += 1

        odd_count = 0
        even_count = 0

        for key, value in char_dict.items():
            current = char_dict[key]
            number_even = value % 2 == 0
            number_odd = value % 2 == 1

            if number_even and not even_count:
                even_count = current
            elif number_odd:
                odd_count += 1
            if number_even and even_count and even_count != current:
                return False
            if odd_count > 1:
                return False
        return True
