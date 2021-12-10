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
        pre_pos = -1

        for c in word:
            if c not in letter_dict:
                return False
            index = bisect.bisect_right(letter_dict[c], pre_pos)
            if index == len(letter_dict[c]):
                return False
            pre_pos = letter_dict[c][index]
        return True
