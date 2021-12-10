class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: intnumber-of-matching-subsequences
        """
        match_count = 0
        word_match = dict()
        letter_dict = defaultdict(list)
        for x in range(0, len(s)):
            letter_dict[s[x]].append(x)
        for word in words:
            if word_match.get(word) is not None:
                if word_match.get(word, None) == True:
                    match_count += 1
                continue
            is_sub = self.isSubsequence(word, s, letter_dict)
            if is_sub:
                word_match[word] = True
                match_count += 1
            else:
                word_match[word] = False
        return match_count

    def isSubsequence(self, word, s, letter_dict):
        w_p, s_p = 0, 0
        letter_count = 0
        while w_p < len(word) and s_p < len(s):
            for l_i in letter_dict.get(word[w_p], []):
                if l_i >= s_p:
                    s_p = l_i
                    letter_count += 1
                    break
            w_p += 1
            s_p += 1
        if w_p == len(word) and letter_count == len(word):
            return True
        else:
            return False
