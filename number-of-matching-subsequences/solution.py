class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: intnumber-of-matching-subsequences
        """
        match_count = 0
        word_match = dict()
        for word in words:
            w_p = 0
            s_p = 0
            if word_match.get(word) is not None:
                if word_match.get(word) == True:
                    match_count+=1
                continue
            while w_p < len(word) and s_p < len(s):
                if word[w_p] == s[s_p]:
                    w_p +=1
                s_p+=1
            if w_p == len(word):
                match_count+=1
                word_match[word] = True
            else:
                word_match[word] = False
        return match_count
