class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_longest = 0 if len(s) == 0 else 1
        character_set = set([])
        longest_string = ""
        i, j = 0, 0
        character_map = {}

        while i < len(s):
            while j < len(s):
                if character_map.get(s[j]):
                    i = max(character_map.get(s[j]), i)
                current_longest = max(current_longest, j - i + 1)
                character_map[s[j]] = j + 1
                j += 1
            i += 1
        return current_longest
