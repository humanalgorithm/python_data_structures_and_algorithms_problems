class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        j, results = len(s) - 1, []
        while j >= 0:
            if s[j] != " ":
                word_end = j
                while j >= 1 and s[j - 1] != " ":
                    j -= 1
                results.append(s[j:word_end + 1])
                j -= 1
                continue
            j -= 1
        return " ".join(results)
