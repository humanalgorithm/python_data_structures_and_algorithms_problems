class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_sig, s_sig = [0 for x in range(0, 26)], [0 for x in range(0, 26)]
        for char in t:
            t_sig[ord(char) - ord("a")] += 1

        for char in s:
            s_sig[ord(char) - ord("a")] += 1

        return t_sig == s_sig
