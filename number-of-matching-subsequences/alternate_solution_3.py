class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: intnumber-of-matching-subsequences
        """
        match_count = 0
        letter_dict = defaultdict(list)
        for x in range(0, len(s)):
            letter_dict[s[x]].append(x)
        for word in words:
            is_sub = self.isSubsequence(word, s, letter_dict)
            if is_sub:
                match_count += 1
        return match_count

    def isSubsequence(self, word, s, letter_dict):
        w_p, s_p = 0, -1

        while w_p < len(word) and s_p < len(s):
            letter_indexes = letter_dict.get(word[w_p], [])
            if not letter_indexes:
                return False
            index = bisect.bisect_right(letter_indexes, s_p)
            if index >= len(letter_indexes):
                return False
            s_p = letter_indexes[index]
            w_p += 1
        return True
