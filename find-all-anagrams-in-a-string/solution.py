class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) == 0 or len(p) > len(s):
            return []

        anagram_sig, anagram_indexes, start_index = [], [], 0
        anagram_sig, p_sig = [0 for num in range(26)], [0 for num in range(26)]
        for char in p:
            p_sig[ord(char) - ord("a")] += 1
        for x in range(0, len(p)):
            anagram_sig[ord(s[x]) - ord('a')] += 1

        while start_index < (len(s) - len(p)) + 1:
            if anagram_sig == p_sig:
                anagram_indexes.append(start_index)
            L = ord(s[start_index]) - ord("a")
            anagram_sig[L] -= 1
            if start_index + len(p) < len(s):
                R = ord(s[start_index + len(p)]) - ord("a")
                anagram_sig[R] += 1
            start_index += 1
        return anagram_indexes
