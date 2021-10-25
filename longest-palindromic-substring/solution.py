class Solution(object):
    palindrome_dict = {}

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        self.longest_palindrome = ""
        char_indexes = self.get_char_indexes(s)
        for key in char_indexes.keys():
            char_indexes_for_key = char_indexes[key]
            i, j = 0, len(char_indexes_for_key) - 1
            while i <= j:
                while j >= i:
                    if char_indexes_for_key[j] - char_indexes_for_key[i] < len(self.longest_palindrome):
                        break
                    self.check_palindrome_for_char(key, s, char_indexes_for_key[i], char_indexes_for_key[j])
                    j -= 1
                i += 1
                j = len(char_indexes_for_key) - 1

        return self.longest_palindrome if len(self.longest_palindrome) > 0 else s[0]

    def get_char_indexes(self, s):
        char_indexes = {}
        for i in range(0, len(s)):
            if not char_indexes.get(s[i]):
                char_indexes[s[i]] = []
            char_indexes[s[i]].append(i)
        return char_indexes

    def check_palindrome_for_char(self, key, s, i, j):
        x, y = i, j
        while i <= j:
            if s[j] != s[i]:
                return
            i, j = i + 1, j - 1
        if y - x + 1 > len(self.longest_palindrome):
            self.longest_palindrome = s[x:y + 1]







