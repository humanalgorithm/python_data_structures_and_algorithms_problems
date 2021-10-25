class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        window, counter = len(s1), 0
        char_mask_s1, char_mask_2 = [0 for i in range(26)], [0 for i in range(26)]
        for char in s1:
            char_mask_s1[ord(char) - ord('a')] += 1

        for char in s2[counter:counter + window]:
            char_mask_2[ord(char) - ord('a')] += 1

        while counter + window <= len(s2):
            if counter > 0:
                char_mask_2[ord(s2[counter - 1]) - ord("a")] -= 1
                char_mask_2[ord(s2[counter + window - 1]) - ord("a")] += 1
            if char_mask_2 == char_mask_s1:
                return True
            counter += 1
        return False
